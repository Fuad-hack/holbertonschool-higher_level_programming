#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data to be sent in POST request
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    # Create the request with POST data
    request = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(request) as response:
        body = response.read()
        print(body.decode('utf-8'))
