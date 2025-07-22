#!/usr/bin/python3
"""
Sends a GET request to a URL and displays the response body.
If HTTP status code >= 400, it prints: Error code: <status code>
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
