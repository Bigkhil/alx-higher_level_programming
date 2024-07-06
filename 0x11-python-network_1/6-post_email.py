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
    email = {"email:": sys.argv[2]}
    response = requests.post(url, data=email)
    print(response.text)


if __name__ == "__main__":
    main()
