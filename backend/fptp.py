from backend.utils import get_keys_with_value

# returns list of winners (multiple winners if tie)
def calculate_fptp(votes, candidates):
    candidate_votes = {}
    for cand in candidates:
        candidate_votes[cand] = 0

    for vote in votes:
        candidate_votes[vote] += 1
    sorted_votes = sorted(candidate_votes.items(), key=lambda x: x[1], reverse=True)

    max_votes = sorted_votes[0][1]
    winners = get_keys_with_value(candidate_votes, max_votes)
    return {'winners': winners, 'order': sorted_votes}