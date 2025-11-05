import re

email_pattern = r'^[a-zA-Z][A-Za-z0-9]*@[a-zA-Z]+\.[A-Za-z]+$'

while True:
    email = input("Enter your email adress: ")
    if (re.fullmatch(email_pattern, email)):
        print("Correct email adress.")
        break
    else:
        print("Invalid email adress!! Try AGAIN")