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