#!/usr/bin/python3
"""Ascript that:
-> takes your github credentials (user name and password)
-> uses the Guthub API to display your id
"""
import sys
import requests
from pprint import pprint


if __name__ == "__main__":
    username = sys.argv[1]
    # url to request
    url = f"https://api.github.com/users/{username}"
    # make the request and return the json
    user_data = requests.get(url).json()
    # pretty print JSON data
    pprint(user_data['id'])
