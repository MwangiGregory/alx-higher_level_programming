#!/usr/bin/python3
"""This script sends a request to a url and displays the value
of the variable X-Request-Id in the response header"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.exceptions import RequestException

    url = sys.argv[1]
    try:
        response = requests.get(url)
    except RequestException as e:
        print("None")
    else:
        print(response.headers.get('X-Request-Id'))
