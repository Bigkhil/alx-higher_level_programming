#!/usr/bin/python3
'''this script fetches a url and prints the response using requests module'''
import requests


def main():
    '''
    this script fetches a url
    and prints the response using requests module
    '''
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print(f"    - type: {type(response.text)}")
    print(f"    - content: {response.text}")


if __name__ == "__main__":
    main()
