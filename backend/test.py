from db.db import Database

db = Database()
db.connect()

# db.create_poll('Atharv ka poll', 'referendum', description='Who is balke balke dot blue?')
p = db.get_poll()
print(p)