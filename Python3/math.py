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

#Bitwise
a = 0b11110000
b = 0b11001100
print(a)  #240
print(bin(a))  #0b11110000
print(bin(a&b))  #0b11000000
print(bin(a|b))  #0b11111100
print(bin(a^b))  #0b111100
print(bin(b >> 3))  #0b11001
print(bin(a << 2))  #0b1111000000