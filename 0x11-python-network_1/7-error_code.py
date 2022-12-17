#!/usr/bin/python3
"""
-> Python script that takes in a URL and an email, sends
-> if http status is greater that or equal to 400 prints Error code.
-> folowed by a value
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
