from utils import get_keys_with_value

# calculate approval voting result
# returns list of winners (multiple winners if tie)
def calculate_approval(votes, cands, max_approved=None, minimum_threshold=None):
    candidates = cands.copy()
    candidates.append('abs')
    candidate_votes = {}
    for cand in candidates:
        candidate_votes[cand] = 0

    for vote in votes:
        if vote == ():
            candidate_votes[candidates[-1]] +=1
        else:
            for v in vote:
                candidate_votes[candidates[v]] += 1

    if not max_approved and not minimum_threshold:
        max_votes = max(candidate_votes.values())
        return get_keys_with_value(candidate_votes, max_votes), candidate_votes
    elif minimum_threshold:
        winners = []
        for (cand, votes) in candidate_votes.items():
            if votes > len(candidates)*minimum_threshold:
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
    # preferences, first number is index of highest preferred candidate
    test_votes = [( 2, 1, 3), (1,), (1, 2), (0, 1), (2, 0), (), (2, 1, 0, 3), (0, 1, 2, 3), (2, 3, 0, 1), (2, 3, 1, 0), (3, 1, 0, 2), (3, 1, 2, 0), (3, 2, 0, 1), (3, 2, 1, 0)]
    winner = calculate_approval(test_votes, candidates, minimum_threshold=.9)
    print(winner)