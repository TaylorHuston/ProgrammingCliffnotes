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