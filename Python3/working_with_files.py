#!/usr/bin/python3

with open("test_output.txt", "w") as file:
    file.write("This is a test file.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")
    file.writelines(["This is the fourth line.\n", "This is the fifth line.\n"])

with open("test_output.txt", "r") as file:
    print(file.read()) #print entire file
    
    #Needs work below
    #print(file.readlines()) #print first line
    
    
    #lines = [line for line in file.readlines()]
    #print(lines)