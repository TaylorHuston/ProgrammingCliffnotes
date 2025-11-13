#!/usr/bin/python3

"""
Demonstrates file handling operations in Python.
"""

# ==========================================
# SECTION 1: WRITING TO FILES
# ==========================================

import os
print("=" * 50)
print("WRITING TO FILES")
print("=" * 50)

# Writing to a file using 'with' statement (context manager)
# This ensures proper file closure even if exceptions occur
with open("test_output.txt", "w") as file:
    file.write("This is a test file.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")
    file.writelines(["This is the fourth line.\n",
                    "This is the fifth line.\n"])

print("File written successfully.")

# ==========================================
# SECTION 2: READING FROM FILES
# ==========================================

print("\n" + "=" * 50)
print("READING FROM FILES")
print("=" * 50)

# Reading an entire file at once
print("\nReading entire file:")
with open("test_output.txt", "r") as file:
    content = file.read()
    print(content)

# Reading file line by line
print("\nReading line by line:")
with open("test_output.txt", "r") as file:
    for line in file:
        print(f"Line: {line.strip()}")

# Reading all lines into a list
print("\nReading all lines into a list:")
with open("test_output.txt", "r") as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")
    print("Lines:")
    for i, line in enumerate(lines):
        print(f"  {i+1}: {line.strip()}")

# Reading specific lines using list comprehension
print("\nReading with list comprehension:")
with open("test_output.txt", "r") as file:
    # Strip newlines from each line
    lines = [line.strip() for line in file.readlines()]
    print(lines)

# ==========================================
# SECTION 3: FILE POSITIONING
# ==========================================

print("\n" + "=" * 50)
print("FILE POSITIONING")
print("=" * 50)

with open("test_output.txt", "r") as file:
    # Read first line
    first_line = file.readline()
    print(f"\nFirst line: {first_line.strip()}")

    # Get current position
    position = file.tell()
    print(f"Current position: {position}")

    # Read next line
    second_line = file.readline()
    print(f"Second line: {second_line.strip()}")

    # Move back to the beginning
    file.seek(0)
    print(f"After seek(0), position: {file.tell()}")

    # Read first 10 characters
    start_chars = file.read(10)
    print(f"First 10 characters: '{start_chars}'")

# ==========================================
# SECTION 4: APPENDING TO FILES
# ==========================================

print("\n" + "=" * 50)
print("APPENDING TO FILES")
print("=" * 50)

with open("test_output.txt", "a") as file:
    file.write("This line was appended.\n")
    file.write("This is another appended line.\n")

print("Content appended to file.")

# Reading the updated file
print("\nReading updated file:")
with open("test_output.txt", "r") as file:
    content = file.read()
    print(content)

# ==========================================
# SECTION 5: BINARY FILES
# ==========================================

print("\n" + "=" * 50)
print("BINARY FILES")
print("=" * 50)

# Writing binary data
with open("binary_test.bin", "wb") as binary_file:
    binary_file.write(b'\x00\x01\x02\x03\x04\x05')
    print("Binary data written")

# Reading binary data
with open("binary_test.bin", "rb") as binary_file:
    binary_data = binary_file.read()
    print(f"Binary data read: {binary_data}")
    print(f"Bytes as integers: {[b for b in binary_data]}")

# Clean up binary test file
os.remove("binary_test.bin")
print("Binary test file removed")

# If you run this script directly
if __name__ == "__main__":
    print("\nThis script demonstrates file operations in Python.")
