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
        # check if a poll with same name exists
        cursor.execute('SELECT id FROM polls WHERE name = ?', (name,))
        if cursor.fetchone():
            raise Exception('Poll already exists')

        cursor.execute('INSERT INTO polls (name, type, description) VALUES (?, ?, ?)', (name, type, description))
        cursor.close()
        self.conn.commit()
