#!/usr/bin/python3
'''
takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
'''
import urllib.parse
import urllib.request
import sys


def main():
    '''this is the main function'''
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email' : email}).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode())


if __name__ == "__main__":
    main()
