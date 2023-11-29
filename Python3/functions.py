import calendar
from datetime import datetime
from datetime import timezone

def myFunction(param):
    test = 9 
    print(test)  #9
    param = param*2
    return param

def dayname(time):
    return calendar.day_name[time.weekday()]

def addition(x, y):
    return x + y

def doubler(x):
    return x * 2

def function_adder(x, func):
    return func(x) + 1

#*args passes in unknown number of arguments, turns them into a tuple
#**kwargs passes in unknown number of arguments, turns them into a dictionary
def printer(*args, **kwargs):
    print(args)
    print(kwargs)

#Does is include all digits 0-9?
def has_all_digits(numbers):
    for n in numbers:
        if set(str(n)) == set("0123456789"):
            return n
    return

#Custom generator, supplies values only when needed, better for memory
def squares_generator():
    for n in range(10**8 +1):
        yield n**2

test = 10
print(test)  #10
print(myFunction(test))  #20
print(test)  #10

print(dayname(datetime.now()))

adder = addition #You can assign a variable to a function
some_number = addition(5,10)
print(some_number)  #15

another_number = function_adder(5, doubler)
print(another_number)  #11

printer("Hello", "World", "Test", a="Yes", b="No")  #('Hello', 'World', 'Test') {'a': 'Yes', 'b': 'No'}

print(has_all_digits([1424872341, 1236490835741, 12341960523]))
squares = squares_generator()
#This will print out the first square that has all the digits 0-9
print(has_all_digits(squares))