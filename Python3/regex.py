#!/usr/bin/python3

"""
Demonstrates regular expression patterns and usage in Python.
"""

import re

zip_code = r"\d{5}"  # regex for five digits in a row

# <re.Match object; span=(19, 24), match='12345'>
print(re.search(zip_code, "This is a zip code 12345"))

if re.search(zip_code, "This is a zip code 12345"):
    print("Found it")
else:
    print("Not found")

s = "This is a zip code 12345, another zip code is 99687"
print(re.findall(zip_code, s))  # ['12345', '99687']

print(re.split(r"\s+", "ant bat cat duck"))  # ['ant', 'bat', 'cat', 'duck']

sonnet = """Let me not to the marriage of true minds
Admit impediments. Love is not love
Which alters when it alteration finds,

Or bends with the remover to remove.
O no, it is an ever-fixed mark
That looks on tempests and is never shaken
It is the star to every wand'ring bark,
Whose worth's unknown, although his height be taken.
Love's not time's fool, though rosy lips and cheeks
Within his bending sickle's compass come:
Love alters not with his brief hours and weeks,
But bears it out even to the edge of doom.
   If this be error and upon me proved,
   I never writ, nor no man ever loved."""

print(re.split("\n", sonnet))  # Split on new line
