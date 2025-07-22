#!/usr/bin/python3
"""
This script sends a request to a URL and displays
the value of the X-Request-Id header in the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
