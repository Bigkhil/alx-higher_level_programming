#!/usr/bin/python3
# this script takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -o /dev/null -w '%{size_download}\n' "$1"
