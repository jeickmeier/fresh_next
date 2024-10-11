from fastapi import APIRouter

router = APIRouter()

@router.get("/genai/", tags=["genai"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]