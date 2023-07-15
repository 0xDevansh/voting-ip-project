from db.Database import Database
from runoff import calculate_runoff
from fptp import calculate_ftpt

if __name__ == '__main__':
    db = Database()
    db.connect()
    votes = [('dk', 'ro', 'tb'),
             ('ro', 'tb', 'dk'),
             ('tb', 'dk', 'ro'),
             ('tb', 'ro', 'dk'),
             ('ro', 'dk', 'tb'),
             ('dk', 'tb', 'ro'),
             ('tb', 'ro', 'dk'),
             ('dk', 'ro', 'tb'),
             ('ro', 'dk', 'tb'),
             ('ro', 'tb', 'dk'),
             ('tb', 'dk', 'ro'),
             ('dk', 'ro', 'tb'),
             ('ro', 'tb', 'dk'),
             ('dk', 'tb', 'ro'),
             ('tb', 'ro', 'dk'),
             ('tb', 'dk', 'ro'),
             ('ro', 'dk', 'tb'),
             ('dk', 'ro', 'tb'),
             ('ro', 'tb', 'dk'),
             ('tb', 'dk', 'ro')]
    # poll = db.create_poll('p1', 'runoff', 'Runoff test poll', secure_mode=True, security_key='lmao', num_voters=20)
    poll = db.get_poll(1)
    print(poll)
    # db.register_candidates(1, [
    #     {'candidate_id': 'ro', 'name': 'Raman Ojha'},
    #     {'candidate_id': 'dk', 'name': 'Dave Kenney'},
    #     {'candidate_id': 'tb', 'name': 'Tutle Bajpai'},
    # ])
    print(db.get_poll_votes(1))
