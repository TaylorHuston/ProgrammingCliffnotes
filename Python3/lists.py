#!/usr/bin/python3

myList1 = [1,2.3,3,4,"bob"]
myList2 = [17, "34"]
print(myList1) #[1,2.3,3,4,"bob"]
print(myList1[4]) #bob
print(myList1+myList2) #[1, 2.3, 3, 4, 'bob', 17, '34']
myList2.append(65)
print(myList2) #[17, '34', 65]
myList2.insert(0, 23)
print(myList2) #[23, 17, '34', 65]
del myList2[0]
print(myList2) #[17, '34', 65]
print(myList2.pop())
print(myList2)

myList1[3] = 34234
print(myList1[3]) #34234