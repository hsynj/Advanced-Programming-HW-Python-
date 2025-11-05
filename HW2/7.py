import re

entry = input("Enter your string-> ")
pattern = r'[0-9]+\.[0-9]|[0-9]+'
numbers = re.findall(pattern, entry)
print(numbers)