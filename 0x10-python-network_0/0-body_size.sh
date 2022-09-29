#!/bin/bash
# This scipt takes in a URL, sends a request to that
# URL, and displays the size of the body of the response.
url="$1"
curl -s -o /dev/null "${url}" -w %{size_download}"\n"
