import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "mistral/mistral-7b-instruct:free"

def analyse_repos_with_gpt(repo_data):
    try:
        summaries = []

        for repo in repo_data:
            repo_name = repo["repo_name"]
            files = repo["files"]

            file_summary = ""

            for file in files[:5]:
                file_summary += f"\n\n### File: {file['file_path']}\n{file['content']}"

            prompt = f""" 
                You are a developer assistant. Analyze the following codebase from a GitHub repo and:
                1. Suggest key technologies used.
                2. Suggest improvements.
                3. Identify resume-worthy skills demonstrated.
                4. Give a credibility score out of 10 based on code quality and completeness.

                Repository: {repo_name}
                {file_summary}
            """

            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": "You're a helpful resume and credibility analyzer."},
                    {"role": "user", "content": prompt}
                ]
            }

            response = requests.post(OPENROUTER_URL, json=payload, headers=headers)
            response.raise_for_status()
            summary = response.json()["choices"][0]["message"]["content"]
            summaries.append({"repo": repo_name, "analysis": summary})

        return summaries
    except Exception as e:
        raise Exception(f"GPT analysis failed: {e}")