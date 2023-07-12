from db.db import Database

if __name__ == '__main__':
    db = Database()
    db.connect()

    #db.create_poll('test1', 'runoff', description='Supreme leader of first bench')
    voters = [
        {'voter_id': 'raman_ojha', 'name': 'Raman Ojha'},
        {'voter_id': 'aarav_patel', 'name': 'Aarav Patel'},
        {'voter_id': 'sanya_gupta', 'name': 'Sanya Gupta'},
        {'voter_id': 'arjun_verma', 'name': 'Arjun Verma'},
        {'voter_id': 'isha_sharma', 'name': 'Isha Sharma'},
        {'voter_id': 'vivek_joshi', 'name': 'Vivek Joshi'},
        {'voter_id': 'kavya_singh', 'name': 'Kavya Singh'},
        {'voter_id': 'neha_kapoor', 'name': 'Neha Kapoor'},
        {'voter_id': 'aishwarya_patel', 'name': 'Aishwarya Patel'},
        {'voter_id': 'kiran_reddy', 'name': 'Kiran Reddy'},
        {'voter_id': 'riya_kumar', 'name': 'Riya Kumar'},
        {'voter_id': 'aryan_gupta', 'name': 'Aryan Gupta'},
        {'voter_id': 'amara_sharma', 'name': 'Amara Sharma'},
        {'voter_id': 'rohan_kapoor', 'name': 'Rohan Kapoor'},
        {'voter_id': 'sanjana_gupta', 'name': 'Sanjana Gupta'},
        {'voter_id': 'ishita_sharma', 'name': 'Ishita Sharma'},
        {'voter_id': 'aditya_kumar', 'name': 'Aditya Kumar'},
        {'voter_id': 'aanya_patel', 'name': 'Aanya Patel'},
        {'voter_id': 'arnav_singh', 'name': 'Arnav Singh'}
    ]
    candidates = [
        {'candidate_id': 'dk', 'name': 'Dave Kenney', 'faction': 'core'},
        {'candidate_id': 'bd', 'name': 'Bada Dubey', 'faction': 'core'},
        {'candidate_id': 'tb', 'name': 'Tutle Bajpai', 'faction': 'shexit'}
    ]
    print(db.get_poll(id=1))
    print(db.get_poll_votes(1, count_only=True))
    db.save_vote(1, 'dk')
    db.save_vote(1, 'dk')
    db.save_vote(1, 'dk')
    db.save_vote(1, 'dk')
    db.save_vote(1, 'tb')
    db.save_vote(1, 'tb')
    db.save_vote(1, 'tb')
    db.save_vote(1, 'bd')
    db.save_vote(1, 'bd')
    db.save_vote(1, 'bd')
    db.save_vote(1, 'bd')
    print(db.get_poll_votes(1, count_only=True))
    print(db.get_poll_votes(1))
