#!/usr/bin/python3
"""
-> script that takes in URL sends a request
-> displays value of variable 'X-Request-Id' in the header
"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]

    request = requests.get(url)
    print(request.headers.get("X-Request-Id"))
