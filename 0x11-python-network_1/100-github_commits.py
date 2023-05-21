#!/usr/bin/python3
"""Please list 10 commits (from the most recent to oldest) of the
 repository “rails” by the user “rails” You must use the GitHub API,
 here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)"""

if __name__ == "__main__":
    import sys
    import requests

    repo_name, owner_name = sys.argv[1:]
    payload = {"per_page": 10}
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    res = requests.get(
        f'https://api.github.com/repos/{owner_name}/{repo_name}/commits',
        params=payload)
    try:
        data = res.json()

        for item in data:
            sha = item.get("sha")
            author = item.get("commit").get("author").get("name")
            print(f"{sha}: {author}")
    except ValueError as e:
        pass
