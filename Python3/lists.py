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
cars.sort()
print(cars) #['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)
print(cars) #['toyota', 'subaru', 'bmw', 'audi']

print(sorted(cars))#['audi', 'bmw', 'subaru', 'toyota']
print(cars) #['toyota', 'subaru', 'bmw', 'audi']

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars) #['subaru', 'toyota', 'audi', 'bmw']
print(len(cars))