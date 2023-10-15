# fetch votes for a given poll and calculate its result
from backend.approval import calculate_approval
from backend.db.Database import Database
from backend.fptp import calculate_fptp
from backend.referendum import calculate_referendum
from backend.runoff import calculate_runoff

# calculates a poll's result and saves it to the database
def calculate_result(poll_id):
    # get poll, votes and candidates data
    db = Database.get_instance()
    poll = db.get_poll(id=poll_id)
    if not poll:
        raise Exception('poll not found')
    votes = db.get_poll_votes(poll_id, only_values=True)
    if len(votes) == 0:
        raise Exception('No votes recorded')
    candidates = db.get_poll_candidates(poll_id)
    candidate_ids = [c['candidate_id'] for c in candidates]

    if poll['type'] == 'fptp':
        result = calculate_fptp(votes, candidate_ids)
        db.save_result(poll_id, result['winners'], result['order'])
        return result
    elif poll['type'] == 'runoff':
        result = calculate_runoff(votes, candidate_ids)
        db.save_result(poll_id, result['winners'], result['order'], eliminated=result['eliminated'])
        return result
    elif poll['type'] == 'approval':
        result = calculate_approval(votes, candidate_ids, max_approved=poll['max_approved'], min_threshold=poll['min_threshold'])
        db.save_result(poll_id, result['winners'], result['order'])
        return result
    elif poll['type'] == 'referendum':
        proposals = db.get_poll_proposals(poll['id'])
        result = calculate_referendum(votes, proposals, min_threshold=poll['min_threshold'])
        db.save_result(poll_id, referendum_result=result)
        return result
