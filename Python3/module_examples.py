#!/usr/bin/python3

"""
Demonstrates module imports and usage in Python.
"""

import os
import sys
import re


def print_section(title):
    """Print a section title with decorative formatting"""
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")


# ==========================================
# SECTION 1: OS MODULE
# ==========================================

def demo_os_module():
    """Demonstrate key features of the os module"""
    print_section("OS MODULE EXAMPLES")

    # Get the current working directory
    current_directory = os.getcwd()
    print(f"Current working directory: {current_directory}")

    # List all files and directories in the current directory
    print("\nFiles and directories in the current directory:")
    for i, item in enumerate(os.listdir(current_directory)[:5]):
        print(f"  {i+1}. {item}")
    if len(os.listdir(current_directory)) > 5:
        print("  ... (more items)")

    # Path manipulation with os.path
    print("\nPath manipulation examples:")
    example_path = os.path.join(current_directory, "data", "config.json")
    print(f"  Joined path: {example_path}")
    print(f"  Directory name: {os.path.dirname(example_path)}")
    print(f"  Base name: {os.path.basename(example_path)}")
    print(f"  Split extension: {os.path.splitext(example_path)}")

    # Path existence checks
    print("\nPath existence checks:")
    print(f"  This script exists: {os.path.exists(__file__)}")
    print(f"  This script is a file: {os.path.isfile(__file__)}")
    print(
        f"  Parent dir is a directory: {os.path.isdir(os.path.dirname(__file__))}")

    # Environment variables
    print("\nSome environment variables:")
    env_vars = ["HOME", "USER", "PATH", "PYTHONPATH"]
    for var in env_vars:
        print(f"  {var}: {os.environ.get(var, 'Not set')[:40]}...")

    # We'll skip directory creation/deletion examples to avoid side effects


# ==========================================
# SECTION 2: SYS MODULE
# ==========================================

def demo_sys_module():
    """Demonstrate key features of the sys module"""
    print_section("SYS MODULE EXAMPLES")

    # System information
    print("System information:")
    print(f"  Python version: {sys.version.split()[0]}")
    print(f"  Python implementation: {sys.implementation.name}")
    print(f"  Platform: {sys.platform}")

    # Command-line arguments
    print("\nCommand-line arguments:")
    print(f"  Script name: {sys.argv[0]}")
    print(f"  Number of arguments: {len(sys.argv) - 1}")
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv[1:]):
            print(f"  Argument {i+1}: {arg}")
    else:
        print("  No command-line arguments provided")

    # System path
    print("\nSystem path (first 3 entries):")
    for i, path in enumerate(sys.path[:3]):
        print(f"  {i}: {path}")
    print(f"  ... ({len(sys.path) - 3} more paths)")

    # Standard I/O streams
    print("\nStandard I/O streams:")
    print("  sys.stdin: Input stream")
    print("  sys.stdout: Output stream")
    print("  sys.stderr: Error stream")

    # Memory usage and management
    print("\nMemory usage:")
    sample_objects = [42, "Hello", [1, 2, 3], {1: 2}]
    for obj in sample_objects:
        print(f"  Size of {repr(obj)}: {sys.getsizeof(obj)} bytes")

    # Recursion limit
    print(f"\nRecursion limit: {sys.getrecursionlimit()}")


# ==========================================
# SECTION 3: RE MODULE (REGULAR EXPRESSIONS)
# ==========================================

def demo_re_module():
    """Demonstrate key features of the re module"""
    print_section("RE MODULE EXAMPLES")

    # Basic pattern matching
    text = "The quick brown fox jumps over the lazy dog"
    print("Text: " + text)

    # Simple search
    pattern = r"brown"
    match = re.search(pattern, text)
    print(
        f"\nSearch for '{pattern}': {match.group() if match else 'No match'}")

    # Case insensitive search
    match = re.search(r"QUICK", text, re.IGNORECASE)
    print(
        f"Case-insensitive search for 'QUICK': {match.group() if match else 'No match'}")

    # Finding all occurrences
    pattern = r"the"
    matches = re.findall(pattern, text, re.IGNORECASE)
    print(f"All occurrences of '{pattern}' (case insensitive): {matches}")

    # Character classes
    print("\nCharacter classes:")
    pattern = r"\b[bf]\w+"  # Words starting with 'b' or 'f'
    matches = re.findall(pattern, text.lower())
    print(f"  Words starting with 'b' or 'f': {matches}")

    # Character classes - vowels
    pattern = r"[aeiou]"
    matches = re.findall(pattern, text.lower())
    print(f"  Number of vowels: {len(matches)}")

    # Metacharacters
    print("\nMetacharacters:")
    sample = "Phone: 555-123-4567, Date: 2025-04-21"
    print("Text: " + sample)

    # \d - digit, \w - word character, \s - whitespace
    pattern = r"\d"
    digits = re.findall(pattern, sample)
    print(f"  All digits: {''.join(digits)}")

    # Word boundaries
    pattern = r"\b\w+\b"
    words = re.findall(pattern, sample)
    print(f"  All words: {words}")

    # Quantifiers
    print("\nQuantifiers:")
    text = "aaa bbb cccc dddddd"
    print("Text: " + text)

    pattern = r"\b\w{3}\b"  # Exactly 3 characters
    matches = re.findall(pattern, text)
    print(f"  Words with exactly 3 characters: {matches}")

    pattern = r"\b\w{4,}\b"  # 4 or more characters
    matches = re.findall(pattern, text)
    print(f"  Words with 4 or more characters: {matches}")

    # Groups and substitution
    print("\nGroups and substitution:")
    date_string = "Today is 2025-04-21"
    print("Text: " + date_string)

    # Capturing groups
    pattern = r"(\d{4})-(\d{2})-(\d{2})"
    match = re.search(pattern, date_string)
    if match:
        print(f"  Full date: {match.group(0)}")
        print(f"  Year: {match.group(1)}")
        print(f"  Month: {match.group(2)}")
        print(f"  Day: {match.group(3)}")

    # Substitution
    pattern = r"\d{4}-\d{2}-\d{2}"
    replaced = re.sub(pattern, "YYYY-MM-DD", date_string)
    print(f"  After substitution: {replaced}")


# Main function that demonstrates all modules
def main():
    """Run all module demonstrations"""
    print("PYTHON MODULE EXAMPLES")
    print("=====================")
    print("This script demonstrates usage of several important Python modules")

    demo_os_module()
    demo_sys_module()
    demo_re_module()

    print("\nModule demonstration complete!")


# Run the script directly
if __name__ == "__main__":
    main()
