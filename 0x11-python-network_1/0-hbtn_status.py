#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        data = res.read()
        print("Body response:")
        print(f"    - type: {type(data)}")
        print(f"    - content: {data}")
        print(f"    - utf8 content: {data.decode('utf-8')}")
