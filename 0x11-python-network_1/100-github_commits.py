#!/usr/bin/python3
"""This script lists 10 commits from recent to oldest from a
specified repository"""

if __name__ == "__main__":
    import requests
    import sys

    repo_name, owner = sys.argv[1], sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"
    response = requests.get(url, params={'per_page': 10})
    response_list = response.json()

    for element in response_list:
        sha = element.get('sha')
        usr_name = element.get('commit').get('author').get('name')
        print(f"{sha}: {usr_name}")
