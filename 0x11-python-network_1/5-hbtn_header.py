#!/usr/bin/python3
'''this script fetches a url and prints the response using requests module'''
import requests
import sys


def main():
    '''
    this script fetches a url
    and prints the response using requests module
    '''
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main()
