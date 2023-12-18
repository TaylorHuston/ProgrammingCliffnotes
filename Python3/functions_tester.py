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

print(has_all_digits([1424872341, 1236490835741, 12341960523]))
squares = squares_generator()

#This will print out the first square that has all the digits 0-9
print(has_all_digits(squares))

print(deriver(square, 3))  #6.000009999951316