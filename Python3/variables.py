#!/usr/bin/python3

#Variables are dynamically typed
num1 = 10
num2 = 11
num3 = 12.5
print(type(num1)) #<class 'int'>
print(type(num3)) #<class 'float'>

print(num1+num2+num3) #33.5

#Assign by value
num2 = num1
print(num1) #10
print(num2) #10
num1 = 13
print(num1) #13

str1 = "Hello"
str2 = "37"

print(str1+" "+str2) #Hello 37

#print(num1+str2)  this will throw an error
#print(str1-str2)  this will throw an error

print(str1[0]) #H
print(str1[1:5]) #ello
print(str1[2:]) #llo
print(str1[:4]) #Hell

#Type conversion
num4 = int(str2)
print(num4) #37
num5 = int(num3)
print(num5) #12
str3 = str(num1)
print(type(str3)) #<class 'str'>

#Tuples and Dictionaries
myTuple = (123131, 12321321, 1231) #tuples are not mutable
print(myTuple) #(123131, 12321321, 1231)
print(myTuple[1]) #12321321
print(type(myTuple)) #<class 'tuple'>

myDict = {'Name' : 'Tom', 'Height': 6.2}
print(myDict)  #{'Name': 'Tom', 'Height': 6.2}
print(myDict['Name'])  #Tom
myDict['Name'] = "Jerry"
print(myDict['Name'])  #Jerry

myDict.clear()
print(myDict) #{}
del myDict
#print(myDict)  this will throw an error




#Constant
MAX_CONNECTIONS = 5000


universe_age = 14_000_000_000
print(universe_age) #14000000000