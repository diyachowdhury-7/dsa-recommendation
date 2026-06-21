from pipeline.recommender.bkt import process_submission
from pipeline.recommender.hlr import process_hlr

# In memory stores — replace with PostgreSQL once backend provides connection
user_mastery_store = {}
user_hlr_store = {}

def handle_update_bkt(submission):
    current_mastery = user_mastery_store.get(submission.userId, {})
    updated_mastery, mastered_topics, results = process_submission(
        submission.model_dump(), current_mastery
    )
    user_mastery_store[submission.userId] = updated_mastery
    return updated_mastery, mastered_topics, results

def handle_update_hlr(submission):
    current_hlr = user_hlr_store.get(submission.userId, {})
    updated_hlr, results = process_hlr(
        submission.model_dump(), current_hlr
    )
    user_hlr_store[submission.userId] = updated_hlr
    return updated_hlr, results
