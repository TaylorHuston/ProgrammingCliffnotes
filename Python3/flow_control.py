#!/usr/bin/python3

"""
Demonstrates flow control structures in Python including conditionals and loops.
"""

i = 0

while (i < 10):
    print(i)
    i += 1

for x in range(0, 10):
    print(x)  # Prints 0-9

for x in range(10):  # Starts at 0 by default
    print(x)  # Prints 0-9

for x in range(10, 15):
    if x == 12:
        break  # Stops the loop
    print(x)

for x in range(20, 25):
    if x == 22:
        continue  # Stops this iteration of the loop
    print(x)

for x in range(100, 200, 10):  # Increment by 10
    print(x)

for x in range(200, 100, -10):  # Decrement by 10
    print(x)

for _ in range(5):  # Ignore the loop variable, essentially a built in placeholder
    print("Hello")

for i, n in enumerate(["a", "b", "c"]):  # Get index and value
    print(i, n)

for i, n in enumerate(["a", "b", "c"], 10):  # Start index at 10
    print(i, n)

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
faces = ["Jack", "Queen", "King", "Ace"]
for suit in suits:
    for card in numbers + faces:  # Concatenate lists
        print(f"{card} of {suit}")

sum = 0
for x in range(0, 100):
    sum += x
print(sum)

# String iteration, also works for lists
myStr = "test"
for c in myStr:
    print(c)

# This also works, just not considered "good python"
for i in range(len(myStr)):
    print(myStr[i])

for x in range(0, 10):
    pass  # Loops and If Statements require a block, pass can be used as a placeholder


test = 11

if test > 0:
    if test > 10:
        print("Greater than 10")
    else:
        print("Positive")
elif test < 0:
    print("Negative")
else:
    print("Zero")

x = 7

if x == 1 or x == 2 or x == 3:
    print("true")
else:
    print("false")  # false

some_bool = True  # Boolean

while some_bool:
    inputs = input("Enter STOP to exit loop: ")
    if inputs == "STOP":
        some_bool = False


# Custom interator
def characters(string):
    for c in string:
        yield c
    return


for c in characters("foobar"):
    print(c)
