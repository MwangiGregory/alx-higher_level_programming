#!/bin/bash
# Displays the size of the body of the response.
curl -s -o /dev/null "$1" -w %{size_download}"\n"
