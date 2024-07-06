#!/usr/bin/python3
'''
takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
'''
import urllib.request
import urllib.error
import sys


def main():
    '''this is the main function'''
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}", error.code)


if __name__ == "__main__":
    main()
