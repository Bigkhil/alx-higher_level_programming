#!/usr/bin/python3
'''this script fetches a url and prints the response using requests module'''
import requests


def main():
	url = "https://alx-intranet.hbtn.io/status"
	response = requests.get(url)
	print(f"type: {response}")
	print(f"content: {response.text}")


if __name__ == "__main__":
	main()	
