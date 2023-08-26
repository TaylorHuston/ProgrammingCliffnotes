str1 = "some string"

print(str1.title())
print(str1.upper())
print(str1.lower())

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

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://')) #nostarch.com

some_file = "python_notes.txt"
print(some_file.removesuffix(".txt"))