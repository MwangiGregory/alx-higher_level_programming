#!/usr/bin/python3
"""This script sends a POST request to a url with the email
as a parameter, and displays the body of the response"""

if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    import sys

    url, email = sys.argv[1], sys.argv[2]
    data = {'email': email}
    data = urlencode(data)
    data = data.encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        body = response.read()

    character_set = response.headers.get_content_charset()
    decoded_body = body.decode(character_set)
    print(decoded_body)
