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

    if not max_approved and not min_threshold:
        max_votes = max(candidate_votes.values())
        return get_keys_with_value(candidate_votes, max_votes), candidate_votes
    elif min_threshold:
        winners = []
        for (cand, v) in candidate_votes.items():
            if v > total_votes * min_threshold / 100:
                winners.append(cand)
        winners.sort()

        if max_approved and len(winners) > max_approved:
            winners = winners[:max_approved]
        return winners
    elif max_approved:
        items = list(candidate_votes.items())
        items.sort(key=lambda c:c[1], reverse=True)
        print(items)
        if len(items) > max_approved:
            items = items[:max_approved]
        return [c[0] for c in items]


if __name__ == '__main__':
    candidates = ['Modi', 'Laxman Singh', 'Donald Trump', 'Arvind Kejriwal']
    candidate_ids = ['md', 'ls', 'dt', 'ak']
    # preferences, first number is index of highest preferred candidate
    test_votes = [( 'dt', 'ls', 'ak'), ('ls',), ('ls', 'dt'), ('md', 'ls'), ('dt', 'md'), (), ('dt', 'ls', 'md', 'ak'), ('md', 'ls', 'dt', 'ak'), ('dt', 'ak', 'md', 'ls'), ('dt', 'ak', 'ls', 'md'), ('ak', 'ls', 'md', 'dt'), ('ak', 'ls', 'dt', 'md'), ('ak', 'dt', 'md', 'ls'), ('ak', 'dt', 'ls', 'md')]
    winner = calculate_approval(test_votes, candidate_ids, min_threshold=.7)
    print(winner)