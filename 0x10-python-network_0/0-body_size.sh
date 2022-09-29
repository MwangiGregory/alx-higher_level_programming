#!/usr/bin/bash
url="$1"
curl -s -o /dev/null "${url}" -w %{size_download}"\n"
