#Using Regex (Regular Expressions) module for email validation.
#Conditions for validation email
# all characters are small
# number 0-9
# using "." and "_" only one time before @
# write @ only one tiem in whole email
# position of "." should be in 3 or 4
import re
email = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your Email id : ")
if re.search(email,user_email):
    print("Right email")
else:
    print("Wrong email, write email again.")