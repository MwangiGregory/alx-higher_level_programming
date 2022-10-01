#!/usr/bin/python3
"""This script takes ina letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""

if __name__ == "__main__":
    from json import JSONDecodeError
    import sys
    import requests
    import json

    q = ""
    try:
        q = sys.argv[1]
    except IndexError as e:
        pass

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})

    try:
        str_output = json.loads(response.text)
    except JSONDecodeError as e:
        print("Not a valid JSON")
    else:
        if len(str_output) == 0:
            print("No result")
        else:
            print(f"[{str_output.get('id')}] {str_output.get('name')}")
