import json

# votes will be stored in a file, where one line is an individual vote, encrypted
# first line stores candidate indices

def create_votefile(candidates, votes = None):
    cand_dict = {}
    for (i, c) in enumerate(candidates):
        cand_dict[c] = i
    candidate_data  = json.dumps(cand_dict)