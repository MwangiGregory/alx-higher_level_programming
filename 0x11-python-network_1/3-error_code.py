#!/usr/bin/python3
"""This script sends a request to a url and displays the body
of the response and handles any HTTPError"""

if __name__ == "__main__":
    import sys
    from urllib.request import urlopen
    from urllib.error import HTTPError

    url = sys.argv[1]

    try:
        response = urlopen(url)
    except HTTPError as e:
        status_code = e.code
        print(f"Error code: {status_code}")
    else:
        print(response.read().decode('utf-8'))
