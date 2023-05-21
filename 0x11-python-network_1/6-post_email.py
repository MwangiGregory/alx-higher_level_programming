#!/usr/bin/python3
"""This script takes in a URL and an email address, sends a POST request to
 the passed URL with the email as a parameter, and finally displays the body
 of the response"""

if __name__ == "__main__":
    import sys
    import requests

    url, email = sys.argv[1:]
    payload = {'email': email}
    res = requests.post(url, data=payload)
    print(res.text)
