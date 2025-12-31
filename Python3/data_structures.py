#!/usr/bin/python3

import random

"""
Demonstrates Python's built-in data structures and their operations.
"""

# ==========================================
# SECTION 1: LISTS
# ==========================================

print("=" * 50)
print("LISTS")
print("=" * 50)

# List creation and basic access
myList1 = [1, 2.3, 3, 4, "bob"]  # Lists can contain mixed types
myList2 = [17, "34"]
print(f"List 1: {myList1}")  # [1, 2.3, 3, 4, 'bob']
print(f"List 2: {myList2}")  # [17, '34']
print(f"Element at index 4: {myList1[4]}")  # bob
# [1, 2.3, 3, 4, 'bob', 17, '34']
print(f"Concatenated lists: {myList1 + myList2}")
print(1 in myList1)  # True
print("alice" in myList1)  # False

# List modification
myList2.append(65)  # Add element to the end
print(f"After append: {myList2}")  # [17, '34', 65]
# 65 (negative indices count from the end)
print(f"Last element: {myList2[-1]}")

myList2.insert(0, 23)  # Insert at specific position
print(f"After insert: {myList2}")  # [23, 17, '34', 65]

del myList2[0]  # Delete element at index
print(f"After delete: {myList2}")  # [17, '34', 65]

popped = myList2.pop()  # Remove and return last element
print(f"Popped element: {popped}")  # 65
print(f"After pop: {myList2}")  # [17, '34']

myList1.pop(0)  # Pop from specific position
print(f"After pop(0): {myList1}")  # [2.3, 3, 4, 'bob']

myList1.remove("bob")  # Remove by value
print(f"After remove: {myList1}")  # [2.3, 3, 4]

# List element assignment
myList1[2] = 34234  # Lists are mutable
print(f"After assignment: {myList1}")  # [2.3, 3, 34234]

# Sorting
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # In-place sort (mutates)
print(f"After sort: {cars}")  # ['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)  # Reverse sort
print(f"After reverse sort: {cars}")  # ['toyota', 'subaru', 'bmw', 'audi']

# ['audi', 'bmw', 'subaru', 'toyota']
print(f"Sorted (non-mutating): {sorted(cars)}")
print(f"Original list remains: {cars}")  # ['toyota', 'subaru', 'bmw', 'audi']

# Reset cars list for further examples
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Reset cars: {cars}")

# List reversal
cars.reverse()  # In-place reverse (mutates)
print(f"After reverse(): {cars}")  # ['subaru', 'toyota', 'audi', 'bmw']
# ['bmw', 'audi', 'toyota', 'subaru']
print(f"reversed() (non-mutating): {list(reversed(cars))}")
print(f"List length: {len(cars)}")  # 4

# Range to list
even_numbers = list(range(2, 11, 2))  # start, end, increment
print(f"Even numbers: {even_numbers}")  # [2, 4, 6, 8, 10]

# List operations
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"Min: {min(digits)}")  # 0
print(f"Max: {max(digits)}")  # 9
print(f"Sum: {sum(digits)}")  # 45

# List slicing
print(f"Slice [0:3]: {digits[0:3]}")  # [1, 2, 3]
print(f"Slice [:3]: {digits[:3]}")  # [1, 2, 3]
print(f"Slice [3:]: {digits[3:]}")  # [4, 5, 6, 7, 8, 9, 0]
print(f"Slice [-3:]: {digits[-3:]}")  # [8, 9, 0]
print(f"Slice with step [0:10:2]: {digits[0:10:2]}")  # [1, 3, 5, 7, 9]
# [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f"Reverse slice [::-1]: {digits[::-1]}")

# List copying
digits2 = digits  # Reference copy (both variables point to the same list)
digits3 = digits.copy()  # Value copy (new list with same values)

print(f"digits == digits2: {digits == digits2}")  # True (same values)
print(f"digits == digits3: {digits == digits3}")  # True (same values)
print(f"digits is digits2: {digits is digits2}")  # True (same object)
print(f"digits is digits3: {digits is digits3}")  # False (different objects)

# List iteration
print("\nList iteration using enumerate (recommended):")
for i, e in enumerate(digits[:3]):  # Only first 3 items for brevity
    print(f"digits[{i}] = {e}")

print("\nList iteration using range (less 'pythonic'):")
for i in range(len(digits[:3])):  # Only first 3 items for brevity
    print(f"digits[{i}] = {digits[i]}")

print("\nDirect list iteration:")
for i in digits[:3]:  # Only first 3 items for brevity
    print(i)

# ==========================================
# SECTION 2: TUPLES
# ==========================================

print("\n" + "=" * 50)
print("TUPLES")
print("=" * 50)

# Tuple creation and access
myTuple = (123131, 12321321, 1231)  # Tuples are immutable lists
print(f"Tuple: {myTuple}")  # (123131, 12321321, 1231)
print(f"Element at index 1: {myTuple[1]}")  # 12321321
print(f"Type: {type(myTuple)}")  # <class 'tuple'>
print(12 in myTuple)  # False
print(1231 in myTuple)  # True

# Single element tuple needs trailing comma
single_element = (42,)  # Comma is necessary!
print(f"Single element tuple: {single_element}, type: {type(single_element)}")

# Tuple unpacking
coordinates = (10.5, 20.8, 30.1)
x, y, z = coordinates  # Unpacking
print(f"Unpacked coordinates: x={x}, y={y}, z={z}")

# ==========================================
# SECTION 3: DICTIONARIES
# ==========================================

print("\n" + "=" * 50)
print("DICTIONARIES")
print("=" * 50)

# Dictionary creation and access
myDict = {'Name': 'Tom', 'Height': 6.2}
print(f"Dictionary: {myDict}")  # {'Name': 'Tom', 'Height': 6.2}
print(f"Accessing by key - Name: {myDict['Name']}")  # Tom
print("Tom" in myDict)  # False (checks keys)
print("Name" in myDict)  # True

# Dictionary modification
myDict['Name'] = "Jerry"  # Modify existing value
print(f"After modification - Name: {myDict['Name']}")  # Jerry

# Safer dictionary access
print(f"Using get() - Name: {myDict.get('Name')}")  # Jerry
# Not specified
print(f"Using get() with default - Age: {myDict.get('Age', 'Not specified')}")

# Dictionary operations
myDict.clear()  # Empty the dictionary
print(f"After clear(): {myDict}")  # {}

# More complex dictionary example
moonwalks = {
    "Neil Armstrong": 1969,
    "Buzz Aldrin": 1969,
    "Alan Shepard": 1971,
    "Eugene Cernan": 1972,
    "Michael Jackson": 1983
}

# Dictionary methods
print(f"Keys: {moonwalks.keys()}")
print(f"Values: {moonwalks.values()}")

# Dictionary iteration
print("\nDictionary iteration by key:")
for key in moonwalks:
    print(f"{key} walked on the moon in {moonwalks[key]}")

print("\nDictionary iteration by key-value pairs:")
for name, year in moonwalks.items():
    print(f"{name} walked on the moon in {year}")

# Dictionary merging (Python 3.9+)
tests1 = {"Math": 75, "Physics": 99}
tests2 = {"Chemistry": 87, "Biology": 95}
test_scores = tests1 | tests2  # Merge dictionaries
print(f"Merged dictionaries: {test_scores}")
# {'Math': 75, 'Physics': 99, 'Chemistry': 87, 'Biology': 95}

retests = {"Math": 100, "Physics": 100}
test_scores |= retests  # Update merged dictionary
print(f"After update: {test_scores}")
# {'Math': 100, 'Physics': 100, 'Chemistry': 87, 'Biology': 95}

# ==========================================
# SECTION 4: SETS
# ==========================================

print("\n" + "=" * 50)
print("SETS")
print("=" * 50)

# Set creation
set1 = {1, 1, 2, 3, 5, 6, 5}  # Duplicate values are automatically removed
print(f"Set1: {set1}")  # {1, 2, 3, 5, 6}

set2 = set([27, 5, 55, 41, 2])  # Create set from list
print(f"Set2: {set2}")  # {2, 5, 27, 41, 55}
print(27 in set2)  # True
print(100 in set2)  # False

# Set operations
print(f"Intersection: {set1.intersection(set2)}")  # {2, 5}
print(f"Union: {set1.union(set2)}")  # {1, 2, 3, 5, 6, 27, 41, 55}
print(f"Difference (set1 - set2): {set1.difference(set2)}")  # {1, 3, 6}

# Special set membership example
apollo_11 = {"Neil Armstrong", "Buzz Aldrin"}  # Set
print(f"Intersection of keys and set: {moonwalks.keys() & apollo_11}")
# {'Buzz Aldrin', 'Neil Armstrong'}

# ==========================================
# MISCELLANEOUS
# ==========================================

print("\n" + "=" * 50)
print("TYPE IDENTIFICATION")
print("=" * 50)

print(f"Type of (): {type(())}")  # <class 'tuple'>
print(f"Type of {{}}: {type({})}")  # <class 'dict'>
print(f"Type of set(): {type(set())}")  # <class 'set'>
print(f"Type of []: {type([])}")  # <class 'list'>

# print(random.choice(set1)) won't work as random does not accept sets so we convert to list
print(f"Random element from set1: {random.choice(list(set1))}")

# If you run this script directly
if __name__ == "__main__":
    print("\nThis script demonstrates Python's built-in data structures.")
