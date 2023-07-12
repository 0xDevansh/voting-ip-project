from utils import get_keys_with_value

# returns list of winners (multiple winners if tie)
def calculate_appro(votes, candidates):
    candidate_votes = {}
    for cand in candidates:
        candidate_votes[cand] = 0

    for vote in votes:
        if vote == ():
            candidate_votes[candidates[-1]] +=1
        if type(vote) == tuple:
            for v in vote:
               candidate_votes[candidates[v]] += 1
        if type(vote) == int:
            candidate_votes[candidates[vote]] +=1


    max_votes = max(candidate_votes.values())
    return get_keys_with_value(candidate_votes, max_votes) , candidate_votes

if __name__ == '__main__':
    candidates = ['Modi', 'Laxman Singh', 'Donald Trump', 'Boris Johnson', 'Abstention']
    # preferences, first number is index of highest preferred candidate
    test_votes = [( 2, 1, 3), (1), (1, 2), (0, 1), (2, 0), (), (2, 1, 0, 3), (0, 1, 2, 3), (2, 3, 0, 1), (2, 3, 1, 0), (3, 1, 0, 2), (3, 1, 2, 0), (3, 2, 0, 1), (3, 2, 1, 0)]
    winner = calculate_appro(test_votes, candidates)
    print(winner)