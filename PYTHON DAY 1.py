FULL_NAME=input("ENTER FULL NAME: ")
EMAIL=input("ENTER EMAIL ID: ")
MOBILE_NUMBER=input("ENTER MOBILE NUMBER: ")
AGE=int(input("ENTER AGE: "))
if FULL_NAME.count(" ")>=1 and FULL_NAME[0]!=" " and FULL_NAME[len(FULL_NAME)-1]!=" ":
    if(EMAIL.count("@")>=1 and EMAIL.count(".")>=1 and EMAIL[0]!="@"):
        if(len(MOBILE_NUMBER)==10 and MOBILE_NUMBER.isdigit() and MOBILE_NUMBER[0]!="0"):
            if(18<AGE<=60):
                print("User Profile is VALID")
            else:
               print("User Profile is INVALID")
        else:
            print("User Profile is INVALID")
    else:
        print("User Profile is INVALID")
else:
    print("User Profile is INVALID")
