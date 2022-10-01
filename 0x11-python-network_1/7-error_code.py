#!/usr/bin/python3
"""This script sends a request to a url and displays the body
of the response and also handles a HTTPError"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.exceptions import HTTPError, RequestException

    url = sys.argv[1]
    try:
        response = requests.get(url)
    except RequestException as e:
        pass
    else:
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
