#!/usr/bin/python3

#Note the whitespace, different from curly bracket languages

i = 0

while(i < 10):
    print(i)
    i += 1


for x in range(10, 15):
    if x == 12:
        break  #Stops the loop
    print(x)


for x in range(10, 15):
    if x == 12:
        continue  #Stops this iteration of the loop


myStr = "test"  #Also works for lists
for c in myStr:
    print(c)


for x in range(0, 10):
    pass  #Loops and If Statements require a block, pass can be used as a placeholder
