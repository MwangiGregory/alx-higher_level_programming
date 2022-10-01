#!/usr/bin/python3
"""This script takes your github credentials and users the
GitHub API to display your id"""

if __name__ == "__main__":
    import sys
    import requests

    username, password = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == requests.codes.ok and len(response.text) > 0:
        try:
            response_dict = response.json()
        except ValueError as e:
            pass
        else:
            print(response_dict.get('id'))
    else:
        print("None")
