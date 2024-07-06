#!/usr/bin/python3
'''this script fetches a url and prints the response using requests module'''
import requests
from sys import argv


def main():
    '''
    this script fetches a url
    and prints the response using requests module
    '''
    url = argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
