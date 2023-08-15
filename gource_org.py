import json
import os
from pathlib import Path
import requests
from git import Repo

config = json.load(open("config.json"))
aliases = {
    source_name: target_name
    for target_name, source_names in config["aliases"].items()
    for source_name in source_names
}


def list_repositories(organization_name: str) -> list:
    response = requests.get(
        f"https://api.github.com/orgs/{organization_name}/repos",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {config['token']}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    return json.loads(response.text)


def clone_repos(repositories: list, dst: Path = Path("./")) -> None:
    dst.mkdir(exist_ok=True, parents=True)
    for repository in repositories:
        if repository["name"] in config["exclude_repositories"]:
            print(f"Skipping {repository['name']} because it is in exclude_repositories")
        elif (dst / repository["name"]).is_dir():
            print(f"Skipping {repository['name']} because it already exists")
        else:
            print(f"Cloning {repository['name']}")
            Repo.clone_from(repository["clone_url"], dst / repository["name"])


def create_gource_logs(repos_dir: Path, dst: Path = Path("./.logs")) -> None:
    if not repos_dir.is_dir():
        raise Exception(f"Invalid repos_dir {repos_dir}. Must be a directory.")
    dst.mkdir(exist_ok=True, parents=True)
    for repo_dir in repos_dir.iterdir():
        if repo_dir.name in config["exclude_repositories"]:
            print(f"Skipping {repo_dir.name} because it is in exclude_repositories")
        else:
            print(f"Creating log for {repo_dir.name}")
            os.system(f"gource {repo_dir} --output-custom-log {dst / repo_dir.name}.log")


def combine_gource_logs(logs_dir: Path, dst: Path = Path("./gource.log")) -> None:
    if not logs_dir.is_dir():
        raise Exception(f"Invalid logs_dir {logs_dir}. Must be a directory.")
    logs = []
    for log_file in logs_dir.iterdir():
        with open(log_file) as f:
            for line in f:
                timestamp, author, edit, path = line.split("|")
                edited_file_path = f"{log_file.name[:-len('.log')]}{path}"
                edited_author = aliases.get(author, author)
                log_line = "|".join([timestamp, edited_author, edit, edited_file_path])
                logs.append(log_line)
    dst.write_text("".join(sorted(logs)))


def create_gource_visualization(
    log_file: Path, dst: Path = Path("./visualization.mp4")
) -> None:
    tmp_file = Path("./tmp.ppm")
    gource_command = f"""
        gource {log_file} \
            --key \
            --viewport 1280x720 \
            --seconds-per-day 0.05 \
            --highlight-users \
            --hide filenames,progress \
            --dir-name-depth 1 \
            --file-idle-time 0 \
            --hide-root \
            -o {tmp_file}
    """
    ffmpeg_command = f"""
        ffmpeg \
            -y \
            -r 60 \
            -f image2pipe \
            -vcodec ppm \
            -i {tmp_file} \
            -vcodec libx264 \
            -preset veryslow \
            -pix_fmt yuv420p \
            -crf 17 \
            -threads 0 \
            -bf 0 {dst}
    """
    os.system(gource_command)
    os.system(ffmpeg_command)
    os.remove(tmp_file)


if __name__ == "__main__":
    repos = list_repositories(config["organization"])
    clone_repos(repos, dst=Path("./.repos"))
    create_gource_logs(Path("./.repos"), dst=Path("./.logs"))
    combine_gource_logs(Path("./.logs"), dst=Path("./gource.log"))
    create_gource_visualization(Path("./gource.log"), dst=Path("./visualization.mp4"))
