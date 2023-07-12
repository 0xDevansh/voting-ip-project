from utils import get_keys_with_value

# returns list of winners (multiple winners if tie)
def calculate_ftpt(votes, candidates):
    candidate_votes = {}
    for cand in candidates:
        candidate_votes[cand] = 0

    for vote in votes:
        candidate_votes[candidates[vote]] += 1

    max_votes = max(candidate_votes.values())
    return get_keys_with_value(candidate_votes, max_votes)