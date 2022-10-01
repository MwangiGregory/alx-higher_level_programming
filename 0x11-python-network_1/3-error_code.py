#!/usr/bin/python3
"""This script sends a request to a url and displays the body
of the response and handles any HTTPError"""

if __name__ == "__main__":
    import sys
    from urllib.request import urlopen
    from urllib.error import HTTPError

    url = sys.argv[1]

    try:
        with urlopen(url) as response:
            body = response.read()
    except HTTPError as e:
        status_code = e.code
        print(f"Error code: {status_code}")
    else:
        print(body.decode('utf-8'))
