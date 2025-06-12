from github import Github
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
g = Github(GITHUB_TOKEN)

def fetch_full_repo_data(username):
    try:
        user = g.get_user(username)
        repos = user.get_repos()
        repo_details = []

        for repo in repos:
            repo_data = {
                "repo_name": repo.name,
                "files": []
            }

            try:
                contents = repo.get_contents("")
                while contents:
                    file_content = contents.pop(0)
                    if file_content.type == "dir":
                        contents.extend(repo.get_contents(file_content.path))
                    else:
                        try:
                            file_data = {
                                "file_path": file_content.path,
                                "content": file_content.decoded_content.decode("utf-8", errors="ignore")
                            }
                            repo_data["files"].append(file_data)
                        except Exception as e:
                            print(f"Error reading file {file_content.path} in {repo.name}: {e}")
            except Exception as e:
                print(f"Error reading contents of repo {repo.name}: {e}")

            repo_details.append(repo_data)

        return repo_details

    except Exception as e:
        raise Exception(f"GitHub fetch failed: {e}")