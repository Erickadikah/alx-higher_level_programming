#!/usr/bin/python3
"""
Module for fetching my status on https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    request = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
