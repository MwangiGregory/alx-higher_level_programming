#!/usr/bin/python3
"""This script akes in a URL and an email, sends a POST request to the passed
 URL with the email as a parameter, and displays the body of the response
 (decoded in utf-8)"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url, email = sys.argv[1:]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    with urllib.request.urlopen(url, data) as res:
        print(res.read().decode('utf-8'))
