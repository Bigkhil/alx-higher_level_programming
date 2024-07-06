#!/usr/bin/python3
"""display your github id"""
import requests
import sys

if __name__ == '__main__':

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)
    res = r.json()
    try:
        for i in range(10):
            name = res[i].get('commit').get('author').get('name')
            print('{}: {}'.format(res[i].get('sha'), name))
    except IndexError:
        pass
