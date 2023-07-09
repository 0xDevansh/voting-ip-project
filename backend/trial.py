def calculate_FTPT(votes, candidates):
    candidate_votes = {}
    for cand in candidates:
        # list stores all votes where this candidate is the first preference
        candidate_votes[cand] = []

    for vote in votes:
        candidate_votes[vote].append(vote)

    while True:
        # calculate number of votes for each candidate
        num_votes = {}
        for (c, v) in candidate_votes.items():
            num_votes[c] = len(v)
        # instant runoff if candidate has > 50%
        max_votes = max(num_votes.values())
        return get_key_with_value(num_votes, max_votes)




def get_key_with_value(dictionary, value):
    try:
        index = list(dictionary.values()).index(value)
        return list(dictionary.keys())[index]
    except ValueError:
        return None


if __name__ == '__main__':
    candidates = ['Modi', 'Laxman Singh', 'Donald Trump', 'Boris Johnson']
    # preferences, first number is index of highest preferred candidate
    test_votes = ['Laxman Singh','Laxman Singh','Laxman Singh','Laxman Singh','Modi', 'Laxman Singh', 'Donald Trump', 'Boris Johnson', 'Modi', 'Laxman Singh', 'Donald Trump', 'Boris Johnson']
    winner = calculate_FTPT(test_votes, candidates)
    print(winner)