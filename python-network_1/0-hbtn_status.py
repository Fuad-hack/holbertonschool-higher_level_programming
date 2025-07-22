#!/usr/bin/python3
"""
This script fetches https://intranet.hbtn.io/status using urllib
and displays information about the response body.
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print("Body response:")
        print("    - type: {}".format(type(body)))
        print("    - content: {}".format(body))
        print("    - utf8 content: {}".format(body.decode('utf-8')))
