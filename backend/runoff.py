from utils import get_keys_with_value

def calculate_runoff(votes, candidates):
    candidate_votes = {}
    # used to break ties
    candidate_points = {}
    for cand in candidates:
        # list stores all votes where this candidate is the first preference
        candidate_votes[cand] = []
        candidate_points[cand] = 0
    
    for vote in votes:
        for (i, choice) in enumerate(vote):
            position = len(vote) - i
            candidate_points[candidates[choice]] += position ** 2
        candidate = candidates[vote[0]]
        candidate_votes[candidate].append(vote)
    print(candidate_points)
    while True:
        # calculate number of votes for each candidate
        num_votes = {}
        for (c, v) in candidate_votes.items():
            num_votes[c] = len(v)
        # instant runoff if candidate has > 50%
        max_votes = max(num_votes.values())
        if max_votes >= len(votes) / 2:
            return get_keys_with_value(num_votes, max_votes)[0]

        # eliminate last candidate
        min_votes = min(num_votes.values())
        for (c, v) in num_votes.items():
            if v != min_votes:
                continue
            # distribute votes to other candidates
            for vote in candidate_votes[c]:
                if len(vote) == 0:
                    continue
                new_vote = vote[1:]
                next_cand = candidates[new_vote[0]]
                # ensure next candidate is not eliminated already
                if next_cand in candidate_votes:
                    candidate_votes[next_cand].append(new_vote)
            del candidate_votes[c]
            # ensure only 1 candidate is eliminated in 1 round
            break

if __name__ == '__main__':
    candidates = ['Modi', 'Laxman Singh', 'Donald Trump', 'Boris Johnson']
    # preferences, first number is index of highest preferred candidate
    test_votes = [(0, 2, 1, 3), (0, 1, 2, 3), (1, 0, 3, 2), (1, 2, 0, 3), (1, 2, 3, 0), (0, 3, 2, 1), (2, 0, 1, 3), (2, 0, 3, 1), (2, 1, 0, 3), (0, 1, 2, 3), (2, 3, 0, 1), (2, 3, 1, 0), (3, 1, 0, 2), (3, 1, 2, 0), (3, 2, 0, 1), (3, 2, 1, 0)]
    winner = calculate_runoff(test_votes, candidates)
    print(winner)