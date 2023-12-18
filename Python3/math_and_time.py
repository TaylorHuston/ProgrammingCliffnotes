import math
import time
from datetime import datetime
from datetime import timezone
import calendar

x=10
y=3

print(x+y)  #13
print(x-y)  #7
print(x*y)  #30
print(x%y)  #1 modulus (remainder)
print(x**y)  #1000 exponent
print(x/y)  #3.33333333.....
print(x//y)  #3 integer division
print(x**3) #1000


#Compare
print(x == y) #False
print(x != y) #True
print(x < y) #False
print(x > y)  #True
print(x <= y)  #False
print(x >= y) #True


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

print(math.pi) #3.141592653589793
print(math.e)  #2.718281828459045
print(math.sqrt(9))  #3.0
print(math.floor(3.14))  #3
print(math.ceil(3.14))  #4
print(math.trunc(3.14))  #3
print(math.log(100, 10))  #2.0
print(math.log10(100))  #2.0
print(math.inf)  #inf
print(math.tau) #6.283185307179586
print(math.sin(math.pi/2))  #1.0

print(int('6'))  #6
print(int(6.145))  #6
#print(int('6.145 ')) errors
print(int(float('6.145')))  #6
print(float('6.145'))  #6.145
print(str(6.145))  #6.145

print(time.time()) #Time since epoch
print(time.ctime()) #Time since epoch human readable
print(time.localtime())

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)

now = datetime.now(timezone.utc)
print(now.hour)

moon_landing = datetime(1969, 7, 20, 20, 17, 40, tzinfo=timezone.utc)
print(moon_landing)

print(now-moon_landing) #Time since moon landing

print(moon_landing.weekday()) #6  (Sunday)
print(list(calendar.day_name)) #['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(calendar.day_name[0]) #Monday 

dayname = calendar.day_name[datetime.now().weekday()]
print(dayname)