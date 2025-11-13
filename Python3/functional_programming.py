#!/usr/bin/python3

"""
Demonstrates functional programming concepts in Python.
"""

states = ["Kansas", "Nebraska", "North Dakota", "South Dakota"]


def urlify(string):
    """Converts a string into a URL-friendly string."""
    return string.lower().replace(" ", "-")

# urls: imperative version


def imperative_urls(states):
    urls = []
    for state in states:
        urls.append(urlify(state))
    return urls


print(imperative_urls(states))

# urls: functional version, list comprehension


def functional_urls(states):
    return [urlify(state) for state in states]


print(functional_urls(states))

# singles: imperative version


def imperative_singles(states):
    singles = []
    for state in states:
        if len(state.split()) == 1:
            singles.append(state)
    return singles


print(imperative_singles(states))

# list comprehension to print only even numbers
print([n for n in range(10) if n % 2 == 0])

# singles: functional version


def functional_singles(states):
    return [state for state in states if len(state.split()) == 1]


print(functional_singles(states))

# lengths: imperative version


def imperative_lengths(states):
    lengths = {}
    for state in states:
        lengths[state] = len(state)
    return lengths


print(imperative_lengths(states))

# lengths: functional version


def functional_lengths(states):
    return {state: len(state) for state in states}


print(functional_lengths(states))

# generator comprehension
squares = (n ** 2 for n in range(10 ** 8 + 1))

# set comprehension with intersection
print({n for n in range(5, 21)} & {n for n in range(10) if n % 2 == 0})

# set comprehension with union
print({n for n in range(5, 21)} | {n for n in range(10) if n % 2 == 0})

numbers = range(0, 101)

# sum: imperative solution


def imperative_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


print(imperative_sum(numbers))

# sum: functional (and built in) solution
print(sum(numbers))
