#!/usr/bin/python3
"""This script takes in a letter and sends a POST request
 to http://0.0.0.0:5000/search_user with the letter as a parameter"""

if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) >= 2:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}
    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        content = res.json()
        if content:
            print(f"{[content.get('id')]} {content.get('name')}")
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
