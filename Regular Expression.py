import re

def check_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$'
    return bool(re.fullmatch(pattern, password))

password = input("Enter your password: ")

if check_password(password):
    print("Valid Password")
else:
    print("Invalid Password")