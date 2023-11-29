import calendar
from datetime import datetime
from datetime import timezone

def myFunction(param):
    test = 9 
    print(test)  #9
    param = param*2
    return param

def dayname(time):
    return calendar.day_name[time.weekday()]

test = 10
print(test)  #10
print(myFunction(test))  #20
print(test)  #10