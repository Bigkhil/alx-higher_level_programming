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
    email = {'email': argv[2]}
    response = requests.post(url, data=email)
    print(response.text)


if __name__ == "__main__":
    main()
