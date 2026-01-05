#!/usr/bin/python3

"""
Basic Data Types in Python
This file demonstrates variables, strings, and basic type operations in Python.
"""

# ==========================================
# SECTION 1: VARIABLES AND BASIC DATA TYPES
# ==========================================

# Variables are dynamically typed
num1 = 10
num2 = 11
num3 = 12.5
print(type(num1))  # <class 'int'>
print(type(num3))  # <class 'float'>

print(num1 + num2 + num3)  # 33.5

# Assign by value
num2 = num1
print(num1)  # 10
print(num2)  # 10
num1 = 13
print(num1)  # 13

# Constants (by convention, use uppercase). Python does not stricytly enforce constants.
MAX_CONNECTIONS = 5000

# Numeric underscore separator for readability
universe_age = 14_000_000_000
print(universe_age)  # 14000000000

x = True  # Boolean
y = False
print(type(x))  # <class 'bool'>


# ==========================================
# SECTION 2: STRINGS AND STRING OPERATIONS
# ==========================================

str1 = "some string"

# String methods
print(str1.title())  # Some String
print(str1.upper())  # SOME STRING
print(str1.lower())  # some string
print(str1.capitalize())  # Some string
print(str1.swapcase())  # SOME STRING
print(str1.replace("some", "another"))  # another string
print(str1.isupper())  # False
print(str1.islower())  # True
print(str1.find("string"))  # 5
print(str1.find("foo"))  # -1
print("some" in str1)  # True

# String indexing and slicing
print(str1[0])  # s
print(str1[1:5])  # ome
print(str1[2:])  # me string
print(str1[:4])  # some

# f-strings (formatted strings)
first_name = "john"
last_name = "doe"
full_name = f"{first_name} {last_name}"
print(full_name)  # john doe
print(f"Hello, {full_name.title()}")  # Hello, John Doe

# Escape sequences
print("\tPython")  # tab
print("Languages:\nPython\nC\nJavaScript")  # New line

# String stripping
print("Python ".rstrip())  # Strip right whitespace
print("  Python".lstrip())  # Strip left whitespace

# Multiline strings
print('''
      This is a multiline string
      Hello Hello  
      ''')

# Raw strings (r-strings)
print(r"Hello\nHello")  # Hello\nHello - prints the \n literally

# String length
print(len("Hello"))  # 5

# String splitting and joining
print("ant cat bat".split())  # ['ant', 'cat', 'bat']
print("ant,cat,bat".split(","))  # ['ant', 'cat', 'bat']
print("ant\nbat\ncat".splitlines())  # ['ant', 'bat', 'cat']
a = ["ant", "bat", "cat"]
print("".join(a))  # antbatcat
print(" ".join(a))  # ant bat cat
print("a".join(a))  # aantabatacat

# String prefix/suffix operations (Python 3.9+)
url = 'https://nostarch.com'
print(url.removeprefix('https://'))  # nostarch.com

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))  # python_notes

# ==========================================
# SECTION 3: TYPE CONVERSION
# ==========================================

# String to number conversion
str2 = "37"
num4 = int(str2)
print(num4)  # 37

# Float to int conversion (truncates decimal part)
num5 = int(num3)
print(num5)  # 12

# Number to string conversion
str3 = str(num1)
print(type(str3))  # <class 'str'>

# Complex conversions
print(int(6))  # 6
print(int(6.145))  # 6
# print(int('6.145'))  # This would error
print(int(float('6.145')))  # 6
print(float('6.145'))  # 6.145
print(str(6.145))  # '6.145'

# ==========================================
# SECTION 4: INPUT AND OUTPUT
# ==========================================

# Basic input (commented out for non-interactive execution)
# name = input("Enter your name: ")  # Input is always a string
# print(f"Hello, {name}")
# print("Hello " + name)

# More efficient input/output combination (commented out)
# print("Hello ", input("Enter your name: "))

# Print with custom end character (instead of newline)
print("Hello", end="xyz")  # Helloxyz
print("foo", end="")
print("bar", end="")
print("baz")  # foobarbaz

# Type error examples (commented out to prevent errors)
# str1 = "Hello"
# num1 = 13
# print(num1 + str2)  # This will throw an error
# print(str1 - str2)  # This will throw an error
