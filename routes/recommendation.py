from fastapi import APIRouter
from controllers.recommendation_controller import handle_get_candidates, handle_recommend

router = APIRouter()

@router.get("/candidates")
def get_candidates(topic: str, min_difficulty: int = 1, max_difficulty: int = 3, limit: int = 10):
    return handle_get_candidates(topic, min_difficulty, max_difficulty, limit)

@router.get("/recommend/{user_id}")
def recommend(user_id: str, limit: int = 10):
    return handle_recommend(user_id, limit)