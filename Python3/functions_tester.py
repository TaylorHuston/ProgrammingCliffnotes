#!/usr/bin/python3
from functions import *
#It is generally not recomended to import all functions from a file, but for this example it gets the job done

test = 10
print(test)  #10
print(myFunction(test))  #20
print(test)  #10

adder = addition #You can assign a variable to a function
some_number = addition(5,10)
print(some_number)  #15

another_number = function_adder(5, doubler) #You can pass a function as an argument
print(another_number)  #11

printer("Hello", "World", "Test", a="Yes", b="No")  #('Hello', 'World', 'Test') {'a': 'Yes', 'b': 'No'}

print(has_all_digits([1424872341, 1236490835741, 12341960523])) #1236490835741
squares = squares_generator()

#This will print out the first square that has all the digits 0-9
print(has_all_digits(squares))

squares2 = (n**2 for n in range(10**8 +1)) #This is a generator expression, it does the same thing as squares_generator()
print(has_all_digits(squares2))

print(deriver(square, 3))  #6.000009999951316

#You can override the parameter order by specifying the parameter name
print_x(5, 10)  #5
print_x(10, 5)  #10
print_x(y=10, x=15)  #15