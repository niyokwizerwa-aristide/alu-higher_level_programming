#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request and displays the body."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    payload = {"email": sys.argv[2]}
    response = requests.post(url, data=payload)
    print(response.text)
