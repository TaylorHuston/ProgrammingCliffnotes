#!/usr/bin/python3
# Examples of working with the re (regular expressions) module
import re

def print_section(title):
    """Print a section title with decorative formatting"""
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")

# Basic pattern matching
print_section("Basic Pattern Matching")
text = "The quick brown fox jumps over the lazy dog"

# Simple match
match = re.search(r"brown", text)
print(f"Search for 'brown': {match.group() if match else 'No match'}")

# Case insensitive search
match = re.search(r"QUICK", text, re.IGNORECASE)
print(f"Case-insensitive search for 'QUICK': {match.group() if match else 'No match'}")

# Finding all occurrences
matches = re.findall(r"the", text, re.IGNORECASE)
print(f"All occurrences of 'the' (case insensitive): {matches}")

# Character classes
print_section("Character Classes")
# Find words that start with 'b' or 'f'
matches = re.findall(r"\b[bf]\w+", text.lower())
print(f"Words starting with 'b' or 'f': {matches}")

# Find all vowels
matches = re.findall(r"[aeiou]", text.lower())
print(f"All vowels: {matches}")
print(f"Number of vowels: {len(matches)}")

# Metacharacters
print_section("Metacharacters")
# \d - digit, \w - word character, \s - whitespace
sample = "Phone: 555-123-4567, Date: 2025-04-21"
digits = re.findall(r"\d", sample)
print(f"All digits: {digits}")
print(f"All digits joined: {''.join(digits)}")

# Word boundaries
words = re.findall(r"\b\w+\b", sample)
print(f"All words: {words}")

# Quantifiers
print_section("Quantifiers")
# * (0 or more), + (1 or more), ? (0 or 1), {n} (exactly n)
text = "aaa bbb cccc dddddd"
pattern1 = re.findall(r"\b\w{3}\b", text)  # Exactly 3 characters
print(f"Words with exactly 3 characters: {pattern1}")

pattern2 = re.findall(r"\b\w{4,}\b", text)  # 4 or more characters
print(f"Words with 4 or more characters: {pattern2}")

# Greedy vs non-greedy
html = "<div>Hello <b>World</b></div>"
greedy = re.search(r"<.+>", html).group()
non_greedy = re.search(r"<.+?>", html).group()
print(f"Greedy match: {greedy}")
print(f"Non-greedy match: {non_greedy}")

# Groups and capturing
print_section("Groups and Capturing")
date_string = "Today is 2025-04-21"
date_pattern = r"(\d{4})-(\d{2})-(\d{2})"
match = re.search(date_pattern, date_string)
if match:
    print(f"Full date: {match.group(0)}")
    print(f"Year: {match.group(1)}")
    print(f"Month: {match.group(2)}")
    print(f"Day: {match.group(3)}")
    print(f"All groups: {match.groups()}")

# Named groups
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, date_string)
if match:
    print(f"Named groups: {match.groupdict()}")
    print(f"Year from named group: {match.group('year')}")

# Substitution
print_section("Substitution")
text = "The color is #FF0000 and #00FF00"
# Replace hex color codes with color names
replaced = re.sub(r"#FF0000", "red", text)
replaced = re.sub(r"#00FF00", "green", replaced)
print(f"After substitution: {replaced}")

# Using backreferences in substitution
text = "John Smith, David Johnson, Sarah Williams"
# Swap first and last names
swapped = re.sub(r"(\w+) (\w+)", r"\2, \1", text)
print(f"Names swapped: {swapped}")

# Compile for reuse
print_section("Compile for Reuse")
# Precompiling patterns for efficiency when used multiple times
email_pattern = re.compile(r"[\w.-]+@[\w.-]+\.\w+")

emails = [
    "user@example.com",
    "invalid-email",
    "another.user@company.org",
    "not an email"
]

for item in emails:
    if email_pattern.match(item):
        print(f"Valid email: {item}")
    else:
        print(f"Invalid email: {item}")

# Split with regex
print_section("Split with Regex")
text = "apple,banana;orange,grape;pear"
# Split on comma or semicolon
fruits = re.split(r"[,;]", text)
print(f"Split result: {fruits}")

print_section("Practical Examples")
# Extracting information
log_entry = "192.168.1.1 - - [21/Apr/2025:10:11:12 +0000] \"GET /index.html HTTP/1.1\" 200 1234"
ip_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
ip = re.search(ip_pattern, log_entry).group()
print(f"IP address: {ip}")

# Validate phone number
phone_number = "555-123-4567"
if re.match(r"^\d{3}-\d{3}-\d{4}$", phone_number):
    print(f"Valid phone number: {phone_number}")
else:
    print(f"Invalid phone number: {phone_number}")

# Flags
print_section("Regular Expression Flags")
text = """This is a multi-line
text with MIXED case
characters."""

# re.IGNORECASE (or re.I) - Case insensitive matching
matches = re.findall(r"text", text, re.IGNORECASE)
print(f"Case insensitive matches: {matches}")

# re.MULTILINE (or re.M) - ^ and $ match at line boundaries
matches = re.findall(r"^text", text, re.MULTILINE | re.IGNORECASE)
print(f"Multiline matches at start of line: {matches}")

# re.DOTALL (or re.S) - . matches any character, including newlines
dot_all = re.search(r"This.*characters", text, re.DOTALL).group()
print(f"DOTALL matches across lines: '{dot_all}'")
