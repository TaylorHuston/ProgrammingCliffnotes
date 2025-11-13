#!/usr/bin/python3

"""
Demonstrates logical operators and boolean expressions in Python.
"""

print((4 > 5) or (4 == 4))  # True
print((4 > 5) and (4 == 4))  # False
print(not (4 > 5))  # True
print(5 is 5)  # True
print(5 is not 5)  # False

# truth table
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

print(not True)  # False
print(not False)  # True

print(True or True and False)  # True (and has higher precedence than or)

myList = [12, 43, "Bob", 17]
print(12 in myList)  # True
print(342 not in myList)  # True
