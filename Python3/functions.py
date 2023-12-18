import calendar
from datetime import datetime
from datetime import timezone

def myFunction(param):
    '''This is a docstring, it is used to describe what a function does, standard practice in Python'''
    test = 9 
    print(test)  #9
    param = param*2
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
    return x**2

def function_adder(x, func):
    '''Calls a function on a number, then adds 1 to it'''
    return func(x) + 1

#*args passes in unknown number of arguments, turns them into a tuple
#**kwargs passes in unknown number of arguments, turns them into a dictionary
def printer(*args, **kwargs):
    '''Prints out all arguments and keyword arguments'''
    print(args)
    print(kwargs)

def has_all_digits(numbers):
    '''Returns the first number that has all digits 0-9'''
    for n in numbers:
        if set(str(n)) == set("0123456789"):
            return n
    return

#Custom generator, supplies values only when needed, better for memory
def squares_generator():
    '''Generates squares of numbers from 0 to 10**8'''
    for n in range(10**8 +1):
        yield n**2

def deriver(f ,x):
    '''Derives a function at a point'''
    h = 0.00001
    return (f(x+h) - f(x))/h

