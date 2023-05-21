#!/usr/bin/python3
"""This script takes in a URL, sends a request to
 the URL and displays the body of the respons"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code:", res.status_code)
    else:
        print(res.text)
