from fastapi import APIRouter, Query
from services.github_fetch import fetch_full_repo_data

router = APIRouter()

@router.get("/github")
async def github_profile(username: str = Query(...)):
    return fetch_full_repo_data(username)