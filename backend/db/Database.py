import json
import sqlite3
from pathlib import Path

SQLITE_FILE = 'database.sqlite'

class Database():
    _instance = None

    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(SQLITE_FILE)
        cursor = self.conn.cursor()
        with open(Path(__file__).resolve().parent.joinpath('definition.sql'), 'r') as file:
            sql = file.read()
            cursor.executescript(sql)
        cursor.close()
        self.conn.commit()
        print('Connected to database')
        self.instance = self

    @staticmethod
    def get_instance():
        if not Database._instance:
            Database._instance = Database()
            Database._instance.connect()
        return Database._instance

    # gets all polls, or the one with the id or name specified
    def get_poll(self, id=None, name=None):
        cursor = self.conn.cursor()
        if id:
            cursor.execute('SELECT id, name, type, description, status, inst_name, num_candidates, security_key, num_voters, max_approved, min_threshold, date_created FROM polls WHERE id = ?', (id,))
            values = cursor.fetchone()
        elif name:
            cursor.execute('SELECT id, name, type, description, status, inst_name, num_candidates, security_key, num_voters, max_approved, min_threshold, date_created FROM polls WHERE name = ?', (name,))
            values = cursor.fetchone()
        else:
            cursor.execute('SELECT id, name, type, description, status, inst_name, num_candidates, security_key, num_voters, max_approved, min_threshold, date_created FROM polls')
            rows = cursor.fetchall()
            res = []
            for row in rows:
                res.append({'id': row[0], 'name': row[1], 'type': row[2], 'description': row[3], 'status': row[4], 'inst_name': row[5], 'num_candidates': row[6], 'security_key': row[7], 'num_voters': row[8], 'max_approved': row[9], 'min_threshold': row[10], 'date_created': row[11]})
            return res
        cursor.close()
        if values:
            return {'id': values[0], 'name': values[1], 'type': values[2], 'description': values[3], 'status': values[4], 'inst_name': values[5], 'num_candidates': values[6], 'security_key': values[7], 'num_voters': values[8], 'max_approved': values[9], 'min_threshold': values[10], 'date_created': values[11]}
        else:
            return None

    def save_result(self, id, winners, order, eliminated=None):
        json_winners = json.dumps(winners)
        json_order = json.dumps(order)
        json_eliminated = None
        if eliminated != None:
            json_eliminated = json.dumps(eliminated)

        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO poll_result (poll_id, winners, order_cands, eliminated) VALUES (?, ?, ?, ?)', (id, json_winners, json_order, json_eliminated))
        cursor.close()
        self.conn.commit()

    def get_result(self, id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT poll_id, winners, order_cands, eliminated FROM poll_result WHERE poll_id = ?', (id,))
        row = cursor.fetchone()
        cursor.close()
        if not row:
            return None
        winners = json.loads(row[1])
        order = json.loads(row[2])
        eliminated = json.loads(row[3])
        return {'winners': winners, 'order': order, 'eliminated': eliminated}

    def create_poll(self, name, type, description=None, status='not_started', security_key=None, secure_mode=False, inst_name=None, num_candidates=0, num_voters=None, max_approved=None, min_threshold=None):
        type_values = ['runoff', 'fptp', 'approval', 'referendum']
        status_values = ['not_started', 'running', 'completed']
        cursor = self.conn.cursor()
        # input validation
        if secure_mode and not security_key:
            raise Exception('security_key required for secure mode')
        if type not in type_values:
            raise Exception(f'Invalid type: {type}, must be one of {type_values}')
        if status not in status_values:
            raise Exception(f'Invalid status: {status}, must be one of {status_values}')
        cursor.execute('SELECT id FROM polls WHERE name = ?', (name,))
        if cursor.fetchone():
            raise Exception('Poll with the same name already exists')

        secure_mode = 1 if secure_mode else 0
        cursor.execute('INSERT INTO polls (name, type, description, status, security_key, secure_mode, num_voters, max_approved, min_threshold, inst_name, num_candidates) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (name, type, description, status, security_key, secure_mode, num_voters, max_approved, min_threshold, inst_name, num_candidates))
        cursor.close()
        self.conn.commit()
        return self.get_poll(name=name)

    def register_candidates(self, poll_id, candidates):
        cursor = self.conn.cursor()
        # validate candidates
        candidate_ids = []
        records = []
        cursor.execute('SELECT candidate_id FROM poll_candidate WHERE poll_id = ?', (poll_id,))
        existing_candidates = cursor.fetchall()
        existing_candidates = [c[0] for c in existing_candidates]
        for cand in candidates:
            if 'candidate_id' not in cand or 'name' not in cand:
                raise Exception('candidate should have candidate_id and name fields')
            if 'faction' not in cand:
                cand['faction'] = None
            if cand['candidate_id'] == 'abs':
                raise Exception('abs is a reserved id')
            if cand['candidate_id'] in candidate_ids or cand['candidate_id'] in existing_candidates:
                raise Exception(f"Duplicate candidate id: {cand['candidate_id']}")
            candidate_ids.append(cand['candidate_id'])
            records.append((poll_id, cand['candidate_id'], cand['name'], cand['faction']))
        # save voters
        cursor.executemany('INSERT INTO poll_candidate (poll_id, candidate_id, name, faction) VALUES (?, ?, ?, ?)', records)
        cursor.close()
        self.conn.commit()

    def register_proposals(self, poll_id, proposals):
        cursor = self.conn.cursor()
        # validate candidates
        proposal_names = []
        records = []
        cursor.execute('SELECT candidate_id FROM poll_proposal WHERE poll_id = ?', (poll_id,))
        existing_proposals = cursor.fetchall()
        existing_proposals = [c[0] for c in existing_proposals]
        for prop in proposals:
            if 'name' not in prop or 'description' not in prop:
                raise Exception('proposal should have name and description fields')
            if prop['name'] == 'abs':
                raise Exception('abs is a reserved name')
            if prop['name'] in proposal_names or prop['name'] in existing_proposals:
                raise Exception(f"Duplicate proposal name: {prop['name']}")
            proposal_names.append(prop['name'])
            records.append((poll_id, prop['name'], prop['description']))
        # save proposals
        cursor.executemany('INSERT INTO poll_proposal (poll_id, name, description) VALUES (?, ?, ?)', records)
        cursor.close()
        self.conn.commit()

    # returns votes for a given poll: (vote, timestamp)
    def get_poll_votes(self, poll_id, candidate_id=None, only_values=False):
        cursor = self.conn.cursor()
        if not has_rows(cursor, 'SELECT id FROM polls WHERE id = ?', (poll_id,)):
            raise Exception(f'No poll found with id: {poll_id}')
        if candidate_id:
            cursor.execute('SELECT vote, created_at FROM votes WHERE poll_id = ? AND candidate_id = ?', (poll_id, candidate_id))
        else:
            cursor.execute('SELECT vote, created_at FROM votes WHERE poll_id = ?', (poll_id,))
        res = cursor.fetchall()
        cursor.close()
        if only_values:
            return [json.loads(v[0]) for v in res]
        else:
            return [(json.loads(v[0]), v[1]) for v in res]

    def get_poll_candidates(self, poll_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT candidate_id, name, faction FROM poll_candidate WHERE poll_id = ?', (poll_id,))
        res = cursor.fetchall()
        cursor.close()
        return [{'candidate_id': c[0], 'name': c[1], 'faction': c[2]} for c in res]

    def save_vote(self, poll_id, vote):
        cursor = self.conn.cursor()
        cursor.execute('SELECT num_voters, status FROM polls WHERE id = ?', (poll_id,))
        data = cursor.fetchone()
        if not data:
            raise Exception('poll not found')
        if data[1] == 'completed':
            raise Exception('election has been completed')
        if data[1] == 'not_started':
            print('Setting status to running')
            cursor.execute('UPDATE polls SET status=\'running\' WHERE poll_id=?', (poll_id,))
        num_voters = data[0]
        cursor.execute('SELECT COUNT(*) FROM votes WHERE poll_id = ?', (poll_id,))
        votes_cast = cursor.fetchone()[0]
        if votes_cast == num_voters:
            raise Exception('exceeded num_voters')
        cursor.execute('INSERT INTO votes (poll_id, vote) VALUES (?, ?)', (poll_id, json.dumps(vote)))
        cursor.close()
        self.conn.commit()

# checks if the given query returns any rows
def has_rows(cursor, query: str, params: tuple) -> bool:
    if len(params):
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    return cursor.fetchone() != None




