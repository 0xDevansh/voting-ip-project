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
            cursor.execute('SELECT id, name, type, description, inst_name, num_candidates, secure_mode, num_voters, max_approved, min_threshold, date_created FROM polls WHERE id = ?', (id,))
            values = cursor.fetchone()
        elif name:
            cursor.execute('SELECT id, name, type, description, inst_name, num_candidates, secure_mode, num_voters, max_approved, min_threshold, date_created FROM polls WHERE name = ?', (name,))
            values = cursor.fetchone()
        else:
            cursor.execute('SELECT id, name, type, description, inst_name, num_candidates, secure_mode, num_voters, max_approved, min_threshold, date_created FROM polls')
            rows = cursor.fetchall()
            res = []
            for row in rows:
                res.append({'id': row[0], 'name': row[1], 'type': row[2], 'description': row[3], 'inst_name': row[4], 'num_candidates': row[5], 'secure_mode': row[6], 'num_voters': row[7], 'max_approved': row[8], 'min_threshold': row[9], 'date_created': row[10]})
            return res
        cursor.close()
        if values:
            return {'id': values[0], 'name': values[1], 'type': values[2], 'description': values[3], 'inst_name': values[4], 'num_candidates': values[5], 'secure_mode': values[6], 'num_voters': values[7], 'max_approved': values[8], 'min_threshold': values[9], 'date_created': values[10]}
        else:
            return None

    def create_poll(self, name, type, description=None, security_key=None, secure_mode=False, inst_name=None, num_candidates=0, num_voters=None, max_approved=None, min_threshold=None):
        cursor = self.conn.cursor()
        # input validation
        if secure_mode and not security_key:
            raise Exception('security_key required for secure mode')
        if type not in ['runoff', 'fptp', 'approval', 'referendum']:
            raise Exception(f'Invalid type: {type}')
        cursor.execute('SELECT id FROM polls WHERE name = ?', (name,))
        if cursor.fetchone():
            raise Exception('Poll with the same name already exists')

        secure_mode = 1 if secure_mode else 0
        cursor.execute('INSERT INTO polls (name, type, description, security_key, secure_mode, num_voters, max_approved, min_threshold, inst_name, num_candidates) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (name, type, description, security_key, secure_mode, num_voters, max_approved, min_threshold, inst_name, num_candidates))
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
            if cand['name'] == 'abs':
                raise Exception('abs is a reserved id')
            if cand['candidate_id'] in candidate_ids or cand['candidate_id'] in existing_candidates:
                raise Exception(f"Duplicate candidate id: {cand['candidate_id']}")
            candidate_ids.append(cand['candidate_id'])
            records.append((poll_id, cand['candidate_id'], cand['name'], cand['faction']))
        # save voters
        cursor.executemany('INSERT INTO poll_candidate (poll_id, candidate_id, name, faction) VALUES (?, ?, ?, ?)', records)
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
        cursor.execute('SELECT num_voters FROM polls WHERE id = ?', (poll_id,))
        data = cursor.fetchone()
        if not data:
            raise Exception('poll not found')
        num_voters = data[0]
        cursor.execute('SELECT COUNT(*) FROM votes WHERE poll_id = ?', (poll_id,))
        votes_cast = cursor.fetchone()[0]
        if votes_cast == num_voters:
            raise Exception('exceeded num_voters')
        cursor.execute('INSERT INTO votes (poll_id, vote) VALUES (?, ?)', (poll_id, json.dumps(vote)))
        cursor.close()
        self.conn.commit()

    def check_security_key(self, poll_id, key):
        cursor = self.conn.cursor()
        cursor.execute('SELECT security_key FROM polls WHERE poll_id = ?', (poll_id,))
        data = cursor.fetchone()
        cursor.close()
        if not data:
            raise Exception("poll doesn't exist")
        return data[0] == key
# checks if the given query returns any rows
def has_rows(cursor, query: str, params: tuple) -> bool:
    if len(params):
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    return cursor.fetchone() != None




