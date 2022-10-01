#!/usr/bin/python3
"""Fetch this url: https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen

with urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()

character_set = response.headers.get_content_charset()
decoded_body = body.decode(character_set)

print(f"""Body response:
\t- type: {type(body)}
\t- content: {body}
\t- utf8 content: {decoded_body}""")
