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

    def register_candidates(self, poll_id: str, candidates: list[dict]):
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
    def get_poll_votes(self, poll_id: str, candidate_id: str = None):
        cursor = self.conn.cursor()
        if not has_rows(cursor, 'SELECT id FROM polls WHERE id = ?', (poll_id,)):
            raise Exception(f'No poll found with id: {poll_id}')
        if candidate_id:
            cursor.execute('SELECT vote, created_at FROM votes WHERE poll_id = ? AND candidate_id = ?', (poll_id, candidate_id))
        else:
            cursor.execute('SELECT vote, created_at FROM votes WHERE poll_id = ?', (poll_id,))
        res = cursor.fetchall()
        cursor.close()
        return res

    def save_vote(self, poll_id, vote):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO votes (poll_id, vote) VALUES (?, ?)', (poll_id, vote))
        cursor.close()
        self.conn.commit()


# checks if the given query returns any rows
def has_rows(cursor, query: str, params: tuple) -> bool:
    if len(params):
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    return cursor.fetchone() != None




