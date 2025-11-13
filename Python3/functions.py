#!/usr/bin/python3

"""
Demonstrates various function definitions and usage patterns in Python.
"""

import calendar
from datetime import datetime
from datetime import timezone


def myFunction(param):
    '''This is a docstring.
      It is used to describe what a function does, standard practice in Python.
      Will be returned if you call help on this function.
      '''
    test = 9
    print(test)  # 9
    param = param * 2
    return param


def dayname(time):
    '''Returns the day of the week as a string'''
    return calendar.day_name[time.weekday()]


def addition(x, y):
    '''Adds two numbers together'''
    return x + y


def doubler(x):
    '''Doubles a number'''
    return x * 2


def square(x):
    '''Squares a number'''
    return x ** 2


def function_adder(x, func):
    '''Calls a function on a number, then adds 1 to it'''
    return func(x) + 1


def print_x(x, y):
    '''Prints out the value assigned to x'''
    print(x)
    return


def default_function(x, y=5):
    '''Adds two numbers together, with a default value for y'''
    return x + y


def return_tuple(x, y):
    '''Returns a tuple of two numbers'''
    return (x, y)


def return_list(x, y):
    '''Returns a list of two numbers'''
    return [x, y]


# Python treats functions as first class objects, meaning they can be passed around like any other object
# You can pass a function as an argument to another function
# You can return a function from another function
# You can assign a function to a variable
# This is a lambda function, it is a small anonymous function
def x(x): return x + 1

# *args passes in unknown number of arguments, turns them into a tuple
# **kwargs passes in unknown number of arguments, turns them into a dictionary


def printer(*args, **kwargs):
    '''Prints out all arguments and keyword arguments'''
    print(args)
    print(kwargs)
    return


def has_all_digits(numbers):
    '''Returns the first number that has all digits 0-9'''
    for n in numbers:
        # Sets can take in any iterable, and will only store unique values
        if set(str(n)) == set("0123456789"):
            return n
    return

# Custom generator, supplies values only when needed, better for memory


def squares_generator():
    '''Generates squares of numbers from 0 to 10**8'''
    for n in range(10 ** 8 + 1):
        yield n ** 2


def deriver(f, x):
    '''Derives a function at a point'''
    h = 0.00001
    return (f(x + h) - f(x)) / h


def hello_world():
    '''Prints Hello, World!
        Doesn't return anything.
        Functions in Python don't have to return a value.
    '''
    print("Hello, World!")
