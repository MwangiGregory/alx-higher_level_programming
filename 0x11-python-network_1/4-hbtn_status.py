#!/usr/bin/python3
"""This script fetches a url using requests module"""

if __name__ == "__main__":
    import requests

    response = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"""Body response:
    \t- type: {type(response)}
    \t- content: {response.text}""")
