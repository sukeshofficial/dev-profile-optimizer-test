from fastapi import FastAPI
from routers import github, resume, analyze

app = FastAPI()

app.include_router(github.router, prefix="/profile")
app.include_router(analyze.router, prefix="/analyze")
# Uncomment resume route when you implement it
# app.include_router(resume.router)