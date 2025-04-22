#!/usr/bin/python3
# filepath: /home/taylor/src/ProgrammingCliffnotes/Python3/math_operations.py

"""
Demonstrates mathematical operations and functions in Python.
"""
import math

# ==========================================
# SECTION 1: BASIC ARITHMETIC
# ==========================================

print("=" * 50)
print("BASIC ARITHMETIC")
print("=" * 50)

x = 10
y = 3

print(f"{x} + {y} = {x + y}")  # 13
print(f"{x} - {y} = {x - y}")  # 7
print(f"{x} * {y} = {x * y}")  # 30
print(f"{x} % {y} = {x % y}")  # 1 (modulus/remainder)
print(f"{x} ** {y} = {x ** y}")  # 1000 (exponentiation)
print(f"{x} / {y} = {x / y}")  # 3.3333... (floating-point division)
print(f"{x} // {y} = {x // y}")  # 3 (integer division)
print(f"{x} ** 3 = {x ** 3}")  # 1000

# ==========================================
# SECTION 2: COMPARISON OPERATIONS
# ==========================================

print("\n" + "=" * 50)
print("COMPARISON OPERATIONS")
print("=" * 50)

print(f"{x} == {y}: {x == y}")  # False
print(f"{x} != {y}: {x != y}")  # True
print(f"{x} < {y}: {x < y}")  # False
print(f"{x} > {y}: {x > y}")  # True
print(f"{x} <= {y}: {x <= y}")  # False
print(f"{x} >= {y}: {x >= y}")  # True

# ==========================================
# SECTION 3: BITWISE OPERATIONS
# ==========================================

print("\n" + "=" * 50)
print("BITWISE OPERATIONS")
print("=" * 50)

a = 0b11110000  # 240 in decimal
b = 0b11001100  # 204 in decimal

print(f"a = {a} ({bin(a)})")  # 240 (0b11110000)
print(f"b = {b} ({bin(b)})")  # 204 (0b11001100)
print(f"a & b = {a & b} ({bin(a & b)})")  # AND: 192 (0b11000000)
print(f"a | b = {a | b} ({bin(a | b)})")  # OR: 252 (0b11111100)
print(f"a ^ b = {a ^ b} ({bin(a ^ b)})")  # XOR: 60 (0b111100)
print(f"b >> 3 = {b >> 3} ({bin(b >> 3)})")  # Right shift: 25 (0b11001)
print(f"a << 2 = {a << 2} ({bin(a << 2)})")  # Left shift: 960 (0b1111000000)

# ==========================================
# SECTION 4: MATH MODULE FUNCTIONS
# ==========================================

print("\n" + "=" * 50)
print("MATH MODULE FUNCTIONS")
print("=" * 50)

# Constants
print(f"math.pi = {math.pi}")  # 3.141592653589793
print(f"math.e = {math.e}")  # 2.718281828459045
print(f"math.tau = {math.tau}")  # 6.283185307179586 (2π)
print(f"math.inf = {math.inf}")  # Positive infinity

# Basic functions
print(f"math.sqrt(9) = {math.sqrt(9)}")  # 3.0
print(f"math.pow(2, 3) = {math.pow(2, 3)}")  # 8.0 (2³)
print(f"math.fabs(-5.5) = {math.fabs(-5.5)}")  # 5.5 (absolute value)

# Rounding
print(f"math.floor(3.14) = {math.floor(3.14)}")  # 3
print(f"math.ceil(3.14) = {math.ceil(3.14)}")  # 4
print(f"math.trunc(3.14) = {math.trunc(3.14)}")  # 3 (truncates toward zero)
print(f"round(3.14159, 2) = {round(3.14159, 2)}")  # 3.14

# Logarithmic functions
print(f"math.log(100, 10) = {math.log(100, 10)}")  # 2.0 (log base 10)
print(f"math.log10(100) = {math.log10(100)}")  # 2.0
print(f"math.log2(8) = {math.log2(8)}")  # 3.0
print(f"math.log(math.e) = {math.log(math.e)}")  # 1.0 (natural logarithm)

# Trigonometric functions
print(f"math.sin(math.pi / 2) = {math.sin(math.pi / 2)}")  # 1.0
print(f"math.cos(math.pi) = {math.cos(math.pi)}")  # -1.0
print(f"math.tan(math.pi / 4) = {math.tan(math.pi / 4)}")  # 1.0
print(f"math.degrees(math.pi) = {math.degrees(math.pi)}")  # 180.0
print(f"math.radians(180) = {math.radians(180)}")  # 3.141592653589793

# ==========================================
# SECTION 5: TYPE CONVERSION
# ==========================================

print("\n" + "=" * 50)
print("TYPE CONVERSION")
print("=" * 50)

print(f"int('6') = {int('6')}")  # 6
print(f"int(6.145) = {int(6.145)}")  # 6 (truncates decimal part)
# print(int('6.145'))  # This would raise an error
print(f"int(float('6.145')) = {int(float('6.145'))}")  # 6
print(f"float('6.145') = {float('6.145')}")  # 6.145
print(f"str(6.145) = '{str(6.145)}'")  # '6.145'

# If you run this script directly
if __name__ == "__main__":
    print("\nThis script demonstrates mathematical operations in Python.")
    print("It is part of the separation of the original math_and_time.py file.")