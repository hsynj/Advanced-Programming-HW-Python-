import re

entry = input("Please enter your entry: ")

pattern = r"[a-z]+[A-Z][A-Z][A-Z]+[a-z]+"

print('=> True' if (re.findall(pattern, entry)) else '=> False')