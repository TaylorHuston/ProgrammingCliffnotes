import requests

URL = "https://cdn.learnenough.com/phrases.txt"

content = requests.get(URL).text
print(content)