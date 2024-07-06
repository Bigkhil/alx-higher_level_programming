#!/usr/bin/python3
'''this script fetches a url and prints the response using requests module'''
import requests
from sys import argv


def main():
    '''
    this script fetches a url
    and prints the response using requests module
    '''
    user_name = argv[1]
    pat = argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(user_name, pat))
    result = response.json()
    print(result.get('id'))


if __name__ == "__main__":
    main()
