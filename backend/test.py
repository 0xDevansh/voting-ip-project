from backend.calculate_result import calculate_result
from db.Database import Database
from runoff import calculate_runoff
from fptp import calculate_fptp

if __name__ == '__main__':
    db = Database().get_instance()
    print('DB connect')
    print(db.conn)
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
    # db.create_poll('p2', 'fptp', 'FPTP test poll', secure_mode=True, security_key='lmao', num_voters=20)
    poll = db.get_poll(2)
    print(poll)
    # db.register_candidates(2, [
    #     {'candidate_id': 'ro', 'name': 'Raman Ojha'},
    #     {'candidate_id': 'dk', 'name': 'Dave Kenney'},
    #     {'candidate_id': 'tb', 'name': 'Tutle Bajpai'},
    # ])
    # db.save_vote(2, 'ro')
    # db.save_vote(2, 'ro')
    # db.save_vote(2, 'ro')
    # db.save_vote(2, 'ro')
    # db.save_vote(2, 'dk')
    # db.save_vote(2, 'dk')
    # db.save_vote(2, 'dk')
    # db.save_vote(2, 'dk')
    # db.save_vote(2, 'dk')
    # db.save_vote(2, 'dk')
    # db.save_vote(2, 'tb')
    # db.save_vote(2, 'tb')
    # db.save_vote(2, 'tb')
    # db.save_vote(2, 'tb')
    print(calculate_result(2))
