#!/usr/bin/python3
'''this script takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.'''
import urllib.request
import sys


def main():
    '''this function sends a request to a url and displays the value of a variable in the header of response'''
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
if __name__ == "__main__":
    main()
