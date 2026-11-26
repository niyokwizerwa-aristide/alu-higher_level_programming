#!/usr/bin/python3
"""Fetches https://hbtn.io using urllib."""
import urllib.request


if __name__ == "__main__":
    url = "https://hbtn.io"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
