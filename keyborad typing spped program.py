from time import *
import random as r
def mistake(paratest,usertest):
    error=0
    for i in range(len(paratest)):
        try:
            if paratest[i] !=usertest[i]:
                error =error + 1
        except :
            error =error + 1
    return error

def speed_time():
    time_delay=time_e - time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)


test=["It is used for choices1","It is used for choices3","It is used for choices3"]
test1=r.choice(test)
print("***********Typing speed*********")
print(test1)
print()
print()
time_1=time()
testinput=input("Enter : ")
time_2=time()
print("Speed : ",time_1,time_2,testinput, "w/sec" )
print("error : ",mistake(test1,testinput))