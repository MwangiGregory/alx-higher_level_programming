#!/usr/bin/python3
"""This script sends a request to a url and displays
the value of the X-Request-Id variable found in the header
of the response"""
from urllib.request import urlopen
import sys

url = sys.argv[1]
with urlopen(url) as response:
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
