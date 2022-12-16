#!/usr/bin/python3

import sys
import urllib.request

if __name__ == '__main__':
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
