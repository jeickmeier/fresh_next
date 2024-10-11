from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/risk/", tags=["risk"])
async def get_risk():
    return [{"username": pd.to_datetime('2024-05-24').strftime('%Y-%m-%d')}]
    #return [{"username": "Rick"}, {"username": "Morty"}]