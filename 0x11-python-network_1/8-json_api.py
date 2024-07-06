#!/usr/bin/python3
'''this script fetches a url and prints the response using requests module'''
import requests
from sys import argv


def main():
    '''
    this script fetches a url
    and prints the response using requests module
    '''
    try:
        ch = argv[1]
    except IndexError:
        ch = ""
    url = "http://0.0.0.0:5000/search_user"
    q = {'q': ch}
    response = requests.post(url, data=q)
    try:
        result = response.json()
        if result == {}:
            print("No result")
        else:
            print(f"[{result[id]}] {result[name]}")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
