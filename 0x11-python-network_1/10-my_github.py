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
    response = requests.get("https://api.github.com/user", auth=(user_name, pat))
    result = response.json()
    print(result.get('id'))


if __name__ == "__main__":
    main()
