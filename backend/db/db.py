import sqlite3
from pathlib import Path

SQLITE_FILE = 'database.sqlite'

# Singleton pattern, only one instance of Database
# can exist and can be called from anywhere
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
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

    # gets all polls, or the one with the id or name specified
    def get_poll(self, id=None, name=None):
        cursor = self.conn.cursor()
        if id:
            cursor.execute('SELECT * FROM polls WHERE id = ?', (id,))
            values = cursor.fetchone()
        elif name:
            cursor.execute('SELECT * FROM polls WHERE name = ?', (name,))
            values = cursor.fetchone()
        else:
            cursor.execute('SELECT * FROM polls')
            rows = cursor.fetchall()
            res = []
            for row in rows:
                res.append({'id': row[0], 'name': row[1], 'type': row[2], 'description': row[3], 'date_created': row[4], 'last_poll': row[5]})
            return res
        cursor.close()
        if values:
            return {'id': values[0], 'name': values[1], 'type': values[2], 'description': values[3], 'date_created': values[4], 'last_poll': values[5]}
        else:
            return None

    def create_poll(self, name, type, description=None):
        cursor = self.conn.cursor()
        # input validation
        if type not in ['runoff', 'fptp', 'approval', 'referendum']:
            raise Exception(f'Invalid type: {type}')
        cursor.execute('SELECT id FROM polls WHERE name = ?', (name,))
        if cursor.fetchone():
            raise Exception('Poll with the same name already exists')

        cursor.execute('INSERT INTO polls (name, type, description) VALUES (?, ?, ?)', (name, type, description))
        cursor.close()
        self.conn.commit()

    def register_voters(self, poll_id, voters):
        cursor = self.conn.cursor()
        # validate voters
        voter_ids = []
        cursor.execute('SELECT voter_id FROM poll_voter WHERE poll_id = ?', (poll_id,))
        existing_voters = cursor.fetchall()
        existing_voters = [v[0] for v in existing_voters]
        records = []
        for voter in voters:
            if 'voter_id' not in voter or 'name' not in voter:
                raise Exception('voter should have voter_id and name fields')
            if voter['voter_id'] in voter_ids or voter['voter_id'] in existing_voters:
                raise Exception(f"Duplicate voter id: {voter['voter_id']}")
            voter_ids.append(voter['voter_id'])
            records.append((poll_id, voter['voter_id'], voter['name']))
        # save voters
        cursor.executemany('INSERT INTO poll_voter (poll_id, voter_id, name) VALUES (?, ?, ?)', records)
        cursor.close()
        self.conn.commit()

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
            if cand['candidate_id'] in candidate_ids or cand['candidate_id'] in existing_candidates:
                raise Exception(f"Duplicate candidate id: {cand['candidate_id']}")
            candidate_ids.append(cand['candidate_id'])
            records.append((poll_id, cand['candidate_id'], cand['name'], cand['faction']))
        # save voters
        cursor.executemany('INSERT INTO poll_candidate (poll_id, candidate_id, name, faction) VALUES (?, ?, ?, ?)', records)
        cursor.close()
        self.conn.commit()
