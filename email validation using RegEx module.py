# a-z
# 0-9
# ._ time1
# @ time1
# . time2 or three

import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
input_email = input("Enter The Email : ")

if re.search(email_condition, input_email):
    print("Right Email")
else:
    print("Wrong email")
