#!/usr/bin/python3
'''this script fetches a link and print it's contents'''
import urllib
import urllib.request


def main():
    '''this function fetches a url using urllib'''
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.read())


if __name__ == "__main__":
    main()
