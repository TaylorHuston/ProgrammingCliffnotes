#!/usr/bin/python3

def myFunction(param):
    test = 9 
    print(test)  #9
    param = param*2
    return param


test = 10
print(test)  #10
print(myFunction(test))  #20
print(test)  #10