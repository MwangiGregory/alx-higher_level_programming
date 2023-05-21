#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id"""

if __name__ == "__main__":
    import sys
    import requests

    username, password = sys.argv[1:]
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {password}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    auth = (username, password)
    res = requests.get(f"https://api.github.com/user", auth=auth)

    try:
        content = res.json()
        print(content.get("id"))
    except ValueError as e:
        pass
