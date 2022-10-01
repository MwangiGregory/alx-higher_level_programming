#!/usr/bin/python3
"""This script fetches a url using requests module"""

if __name__ == "__main__":
    import requests

    response = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"Body response:",
          f"\n- type: {type(response.text)}",
          f"\n- content: {response.text}")
