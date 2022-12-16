#!/usr/bin/python3
"""
-> Python script that takes in a URL
-> Handles urllib.error.HTTPError
-> prints Error code & HTTP status code
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
