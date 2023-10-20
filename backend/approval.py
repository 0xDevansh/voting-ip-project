from backend.utils import get_keys_with_value

# calculates approval voting result
# returns list of winners (multiple winners if tie)
def calculate_approval(votes, candidates, max_approved=None, min_threshold=None):
    print(min_threshold, max_approved)
    # votes should be list of candidate_ids in preference order
    candidate_votes = {}
    for cand in candidates:
        candidate_votes[cand] = 0

    # count votes
    for vote in votes:
        if len(vote) != 0:
            for v in vote:
                candidate_votes[v] += 1
    sorted_votes = sorted(candidate_votes.items(), key=lambda x: x[1], reverse=True)
    candidate_percentages = [(c, v / len(votes) * 100) for (c, v) in candidate_votes.items()]

    if not max_approved and not min_threshold:
        # simply return candidate with most votes
        max_votes = max(candidate_votes.values())
        winners = get_keys_with_value(candidate_votes, max_votes)
        return {'winners': winners, 'order': sorted_votes}
    elif min_threshold:
        # filter winners on having less votes than min_threshold
        winners = [c for (c, v) in sorted_votes if v >= len(votes) * min_threshold / 100]
        if max_approved and len(winners) > max_approved:
            winners = winners[:max_approved]
        return {'winners': winners, 'order': sorted_votes}
    elif max_approved:
        # return top n candidates
        winners = [v[0] for v in sorted_votes]
        if len(winners) > max_approved:
            winners = winners[:max_approved]
        return {'winners': winners, 'order': sorted_votes}