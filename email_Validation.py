#This is email validation code using string function
email = input("Enter your e-mail Id : ")  #The minimum length of an email is 6 and the basic conditions like e@g.in or e@g.com
forvalidation,forvalidation1,forvalidation2=0,0,0
if len(email) >= 6:   #Here checking the length of an email i.e atleast 6
    if email[0].isalpha(): #Here checking the first letter of email i.e first is alphaber
        if ("@" in email) and (email.count("@") == 1): #Here I use membership operator for checking email cantaining only one @ symbol
           if (email[-4] == ".") ^ (email[-3] == "."): #check for . in email from backward and use XOR operator
               for i in email:  # here itrate email and check the all mentioned condition
                   if i == i.isspace():
                       forvalidation = 1
                   elif i.isalpha():
                       if i == i.upper():
                           forvalidation1 = 1
                   elif i.isdigit():
                       continue
                   elif i == "_" or i == "." or i == "@":
                       continue
                   else:
                       forvalidation2 = 1
               if forvalidation == 1 or forvalidation1 == 1 or forvalidation2 == 1:
                    print("Wrong email")
               else:
                   print("This email Id is Right.")
           else:
               print("Wrong email")
        else:
            print("Wrong email")
    else:
        print("Wrong email")
else:
    print("Wrong email")