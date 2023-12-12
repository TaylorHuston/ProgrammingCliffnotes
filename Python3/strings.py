str1 = "some string"

print(str1.title()) #Some String
print(str1.upper()) #SOME STRING
print(str1.lower()) #some string
print(str1.capitalize()) #Some string
print(str1.swapcase()) #SOME STRING
print(str1.replace("some", "another")) #another string
print(str1.isupper()) #False
print(str1.islower()) #True
print(str1.find("string")) #5
print(str1.find("foo")) #-1
print("some" in str1) #True
print(str1[0]) #s


#f-strings
first_name = "john"
last_name = "doe"
full_name = f"{first_name} {last_name}"
print(full_name) #john doe
print(f"Hello, {full_name.title()}") #Hello, John Doe

print("\tPyton") #tab
print("Languages:\nPython\nC\nJavaScript") #New line
print("Python ".rstrip()) #Strip right whitespace
print("  Python".lstrip()) #Strip left whitespace

print('''
      This is a multiline string)
      Hello Hello  
      ''')


name = input("Enter your name: ") #Input is always a string
print(f"Hello, {name}")
print("Hello " + name)

print("Hello ", input("Enter your name: ")) #This is a bit more efficient

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://')) #nostarch.com

some_file = "python_notes.txt"
print(some_file.removesuffix(".txt"))

#r-strings (raw)
print(r"Hello\nHello") #Hello\nHello

#End of string keyword replacement, mostly used to replace the automatic new line in scripts
print("Hello", end="xyz") #Helloxyz
print("foo", end="")
print("bar", end="")
print("baz") #foobarbaz

#Length of string
print(len("Hello")) #5

print("ant cat bat".split()) #['ant', 'cat', 'bat']")
print("ant,cat,bat".split(",")) #['ant', 'cat', 'bat']
print("ant\nbat\ncat".splitlines()) #['ant', 'bat', 'cat']
a = ["ant", "bat", "cat"]
print("".join(a)) #antbatcat
print(" ".join(a)) #ant bat cat
print("a".join(a)) #aantabatacat

