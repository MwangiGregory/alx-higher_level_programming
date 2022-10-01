#!/usr/bin/python3
"""This script sends a request to a url and displays the value
of the variable X-Request-Id in the response header"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers["X-Request-Id"])
