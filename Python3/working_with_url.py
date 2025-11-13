#!/usr/bin/python3

"""
Demonstrates working with URLs and making HTTP requests in Python.
"""

import requests

URL = "https://cdn.learnenough.com/phrases.txt"

content = requests.get(URL).text
print(content)
