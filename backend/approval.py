from utils import get_keys_with_value

# calculate approval voting result
# returns list of winners (multiple winners if tie)
def calculate_approval(votes, cands, max_approved=None, min_threshold=None):
    # votes should be list of candidate_ids in preference order
    candidates = cands.copy()
    if min_threshold:
        candidates.append('abs')
    candidate_votes = {}
    for cand in candidates:
        candidate_votes[cand] = 0

    total_votes = 0
    for vote in votes:
        if vote == () and min_threshold:
            candidate_votes['abs'] +=1
            total_votes += 1
        else:
            for v in vote:
                candidate_votes[v] += 1
                total_votes += 1
    sorted_votes = sorted(candidate_votes.items(), key=lambda x: x[1], reverse=True)
    if not max_approved and not min_threshold:
        max_votes = max(candidate_votes.values())
        winners = get_keys_with_value(candidate_votes, max_votes)
        return {'winners': winners, 'order': sorted_votes}
    elif min_threshold:
        winners = [c for (c, v) in sorted_votes if v >= total_votes * min_threshold / 100]
        if max_approved and len(winners) > max_approved:
            winners = winners[:max_approved]
        return {'winners': winners, 'order': sorted_votes}
    elif max_approved:
        winners = [v[0] for v in sorted_votes]
        if len(winners) > max_approved:
            winners = winners[:max_approved]
        return {'winners': winners, 'order': sorted_votes}


if __name__ == '__main__':
    candidates = ['Modi', 'Laxman Singh', 'Donald Trump', 'Arvind Kejriwal']
    candidate_ids = ['md', 'ls', 'dt', 'ak']
    # preferences, first number is index of highest preferred candidate
    test_votes = [( 'dt', 'ls', 'ak'), ('ls',), ('ls', 'dt'), ('md', 'ls'), ('dt', 'md'), (), ('dt', 'ls', 'md', 'ak'), ('md', 'ls', 'dt', 'ak'), ('dt', 'ak', 'md', 'ls'), ('dt', 'ak', 'ls', 'md'), ('ak', 'ls', 'md', 'dt'), ('ak', 'ls', 'dt', 'md'), ('ak', 'dt', 'md', 'ls'), ('ak', 'dt', 'ls', 'md')]
    winner = calculate_approval(test_votes, candidate_ids, max_approved=3, min_threshold=20)
    print(winner)