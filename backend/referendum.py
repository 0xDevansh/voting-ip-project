# calculate referendum voting result
# returns list of winners (multiple winners if tie)


def calculate_referendum(votes, proposals, min_threshold=0):
    if isinstance(min_threshold, str):
        min_threshold = 0
    approved = {}
    disapproved = {}
    abstained = {}
    for proposal in proposals:
        approved[proposal['name']] = 0
        disapproved[proposal['name']] = 0
        abstained[proposal['name']] = 0

    # count votes
    for vote in votes:
        for prop in proposals:
            prop_name = prop['name']
            if not prop_name in vote.keys():
                continue
            if vote[prop_name] == 'app':
                approved[prop_name] += 1
            elif vote[prop_name] == 'dis':
                disapproved[prop_name] += 1
            elif vote[prop_name] == 'abs':
                abstained[prop_name] += 1
    result = []
    num_votes = len(votes)
    for prop in proposals:
        name = prop['name']
        approve_percent = round(approved[name] / num_votes * 100, 2)
        disapprove_percent = round(disapproved[name] / num_votes * 100, 2)
        abstain_percent = round(abstained[name] / num_votes * 100, 2)
        print(prop)
        description= prop['faction']
        res = 'dis'
        print(approve_percent, min_threshold)
        if approve_percent > min_threshold:
            res = 'app'
        result.append({'name': name, 'description': description, 'approve_percent': approve_percent, 'disapprove_percent': disapprove_percent, 'abstain_percent': abstain_percent, 'result': res})

    return result

if __name__ == '__main__':
    from db.Database import Database
    db = Database.get_instance()
    poll = db.get_poll(name='referendum')
    props = db.get_poll_proposals(poll['id'])
    votes = db.get_poll_votes(poll['id'], only_values=True)
    print(calculate_referendum(votes, props, poll['min_threshold']))
