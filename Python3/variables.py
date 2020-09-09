#!/usr/bin/python3

#variables are not type specific
num1 = 10
num2 = 11
num3 = 12.5

print(num1+num2+num3) #33.5

str1 = "Hello"
str2 = "12"

print(str1+" "+str2) #Hello 12

#print(num1+str2)  this will throw an error
#print(str1-str2)  this will throw an error

print(str1[0]) #H
print(str1[1:5]) #ello
print(str1[2:]) #llo
print(str1[:4]) #Hell

myList1 = [1,2.3,3,4,"bob"]
myList2 = [17, "34"]
print(myList1) #[1,2.3,3,4,"bob"]
print(myList1[4]) #bob
print(myList1+myList2) #[1, 2.3, 3, 4, 'bob', 17, '34']

myList1[3] = 34234
print(myList1[3]) #34234

myTuple = (123131, 12321321, 1231) #tuples are not mutable
print(myTuple) #(123131, 12321321, 1231)
print(myTuple[1]) #12321321

myDict = {'Name' : 'Tom', 'Height': 6.2}
print(myDict)  #{'Name': 'Tom', 'Height': 6.2}
print(myDict['Name'])  #Tom
myDict['Name'] = "Jerry"
print(myDict['Name'])  #Jerry

myDict.clear()
print(myDict) #{}
del myDict
#print(myDict)  this will throw an error


#Math
x=10
y=3

print(x+y)  #13
print(x-y)  #7
print(x*y)  #30
print(x%y)  #1
print(x**y)  #1000
print(x/y)  #3.33333333.....
print(x//y)  #3

#Compare
print(x == y) #False
print(x != y) #True
print(x < y) #False
print(x > y)  #True
print(x <= y)  #False
print(x >= y) #True
print(str1 == str2) #False
print(str1 != str2) #True
print(str1 > str2)  #True (string length)
