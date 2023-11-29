#!/usr/bin/python3

myList1 = [1, 2.3, 3, 4, "bob"]
myList2 = [17, "34"]
print(myList1) #[1,2.3,3,4,"bob"]
print(myList1[4]) #bob
print(myList1+myList2) #[1, 2.3, 3, 4, 'bob', 17, '34']

myList2.append(65)
print(myList2) #[17, '34', 65]
print(myList2[-1]) #65

myList2.insert(0, 23)
print(myList2) #[23, 17, '34', 65]

del myList2[0]
print(myList2) #[17, '34', 65]

print(myList2.pop())  #65
print(myList2) #[17, '34']

myList1.pop(0)
print(myList1) #[2.3, 3, 4, 'bob']

myList1.remove("bob")
print(myList1) #[2.3, 3, 4]

myList1[2] = 34234
print(myList1)
print(myList1[2]) #34234

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #mutates
print(cars) #['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)
print(cars) #['toyota', 'subaru', 'bmw', 'audi']

print(sorted(cars))#['audi', 'bmw', 'subaru', 'toyota'] does not mutate
print(cars) #['toyota', 'subaru', 'bmw', 'audi']

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(cars[-1]) #subaru

cars.reverse()
print(cars) #['subaru', 'toyota', 'audi', 'bmw']
print(len(cars))

even_numbers = list(range(2, 11, 2)) #start, end, increment
print(even_numbers) #[2, 4, 6, 8, 10]


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) #0
print(max(digits)) #9
print(sum(digits)) #45

print(digits[0:3]) #[1, 2, 3]
print(digits[:3]) #[1, 2, 3]
print(digits[3:]) #[4, 5, 6, 7, 8, 9, 0]
print(digits[-3:]) #[8, 9, 0]
print(digits[0:10:2]) #[1, 3, 5, 7, 9]
print(digits[::-1]) #[0, 9, 8, 7, 6, 5, 4, 3, 2, 1] clever, but kind of hideous

digits2 = digits #Copies reference, not values
digits3 = digits.copy() #Copies values, not reference

print(digits == digits2) #True
print(digits == digits3) #True
print(digits is digits2) #True
print(digits is digits3) #False

for i,e in enumerate(digits):
    print(f"digits[{i}] = {e}")


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
print(myDict.get('Name')) #Jerry

myDict.clear()
print(myDict) #{}
del myDict
#print(myDict)  this will throw an error

moonwalks = {"Neil Armstrong": 1969,
             "Buzz Aldrin": 1969,
             "Alan Shepard": 1971,
             "Eugene Cernan": 1972,
             "Michael Jackson": 1983}
appollo_11 = {"Neil Armstrong", "Buzz Aldrin"}
print(moonwalks.keys()) #dict_keys(['Neil Armstrong', 'Buzz Aldrin', 'Alan Shepard', 'Eugene Cernan', 'Michael Jackson'])
print(moonwalks.values()) #dict_values([1969, 1969, 1971, 1972, 1983])
print(moonwalks.keys() & appollo_11) #{'Buzz Aldrin', 'Neil Armstrong'}
print("Buzz Aldrin" in moonwalks) #True

#Sets
set1= {1,1,2,3,5,6,5}
print(set1) #{1, 2, 3, 5, 6}

set2 = {27,5,55,41,2}
print(set1.intersection(set2)) #{2, 5}
print(set1.union(set2)) #{1, 2, 3, 5, 6, 41, 55, 27}
print(set1.difference(set2)) #{1, 3, 6}

print(type(())) #<class 'tuple'>
print(type({})) #<class 'dict'>
print(type(set())) #<class 'set'>


