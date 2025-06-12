from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.github_fetch import fetch_full_repo_data
from services.gpt_analyser import analyse_repos_with_gpt

router = APIRouter()

class AnalyzeRequest(BaseModel):
    username: str

@router.post("/")
def analyze_user_profile(req: AnalyzeRequest):
    try:
        repo_data = fetch_full_repo_data(req.username)
        analysis = analyse_repos_with_gpt(repo_data)
        return {
            "username": req.username,
            "analysis": analysis
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))