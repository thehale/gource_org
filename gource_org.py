import json
import os
from pathlib import Path
import requests
from git import Repo

config = json.load(open('config.json'))

def list_repositories(organization_name: str) -> list:
    response = requests.get(
        f"https://api.github.com/orgs/{organization_name}/repos",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {config['token']}",
            "X-GitHub-Api-Version": "2022-11-28",
        }
    )
    return json.loads(response.text)

def clone_repos(repositories: list, dst: Path = Path("./")) -> None:
    dst.mkdir(exist_ok=True, parents=True)
    for repository in repositories:
        print(f"Cloning {repository['name']}")
        Repo.clone_from(repository["clone_url"], dst / repository["name"])

if __name__ == "__main__":
    repos = list_repositories(config["organization"])
    clone_repos(repos, dst=Path("./.repos"))