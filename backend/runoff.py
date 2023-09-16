from backend.utils import get_keys_with_value

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
            candidate_points[choice] += position ** 2
        candidate_votes[vote[0]].append(vote)

    sorted_cand_points = sorted(candidate_points.items(), key=lambda x: x[1]) # lowest points first
    eliminated = []
    order = None
    while True:
        # calculate number of votes for each candidate
        num_votes = {}
        for (c, v) in candidate_votes.items():
            num_votes[c] = len(v)

        if not order:
            order = sorted(num_votes.items(), key=lambda x:x[1], reverse=True)
        # instant runoff if candidate has > 50%
        max_votes = max(num_votes.values())
        if max_votes >= len(votes) / 2:
            remaining = sorted(num_votes.items(), key=lambda x:x[1], reverse=True)
            winner = get_keys_with_value(num_votes, max_votes)[0]
            return {'winners': winner, 'order':order, 'eliminated':eliminated, 'remaining': remaining}

        # eliminate last candidate
        min_votes = min(num_votes.values())
        if list(num_votes.values()).count(min_votes) > 1:
            # eliminate based on initial points
            elim_candidates = [c for (c, v) in num_votes.items() if v == min_votes]
            elim_points = [(c, v) for (c, v) in sorted_cand_points if c in elim_candidates]
            # sorted_cand_points is already sorted ascending by points
            elim_cand = elim_points[0][0]
        else:
            elim_cand = get_keys_with_value(num_votes, min_votes)[0]
        eliminated.append(elim_cand)
        # distribute votes to other candidates
        for vote in candidate_votes[elim_cand]:
            if len(vote) == 0:
                continue
            new_vote = vote[1:]
            next_cand = new_vote[0]
            # ensure next candidate is not eliminated already
            if next_cand in candidate_votes:
                candidate_votes[next_cand].append(new_vote)
        del candidate_votes[elim_cand]

if __name__ == '__main__':
    candidates = ['md', 'ls', 'dt', 'bj']
    # preferences, first number is index of highest preferred candidate
    test_votes = [('md', 'ls', 'dt', 'bj'), ( 'md', 'bj', 'dt','ls'), ('ls', 'dt', 'md', 'bj'), ('ls', 'dt', 'bj', 'md'), ('md', 'bj', 'dt', 'ls'), ('dt', 'md', 'ls', 'bj'), ('dt', 'md', 'bj', 'ls'), ('dt', 'ls', 'md', 'bj'), ('md', 'ls', 'dt', 'bj'), ('dt', 'bj', 'md', 'ls'), ('dt', 'bj', 'ls', 'md'), ('bj', 'ls', 'md', 'dt'), ('bj', 'ls', 'dt', 'md'), ('bj', 'dt', 'md', 'ls'), ('bj', 'dt', 'ls', 'md')]
    winner = calculate_runoff(test_votes, candidates)
    print(winner)