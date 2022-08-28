name = str(input("Enter The name of The Applicant: "))
age = int(input("Enter The age of The Applicant " + name + ":"))

if age >= int(18) and age <= int(30):
    print("Please Fill Up the Form. ")
else:
    print("  You are not Allowed for Applying This Job because Your Age is  which is against Our Rules")
    quatha = str(input("Are you The Quatha Candidate?(yes/no): "))
    if quatha == "yes" and age<=32:
        print("You are allowed!!")
    elif quatha == "no":
        print("You are not allowed because Qutha Can maximum age Limit 32 ")
    else:
        print("Only quath can Apply maximum Age of 32")