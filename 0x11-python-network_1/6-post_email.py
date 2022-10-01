#!/usr/bin/python3
"""This script sends a POST request to a url with the email as
a parameter and finally displays the body of the response"""

if __name__ == "__main__":
    import sys
    import requests
    from requests.exceptions import RequestException

    url, email = sys.argv[1], sys.argv[2]

    try:
        response = requests.post(url, data={'email': email})
    except RequestException as e:
        pass
    else:
        print(response.text)
