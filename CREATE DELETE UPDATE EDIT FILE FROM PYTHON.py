import os

#create file....
#file=open("demo.txt", "x")
#file=open("demo.txt", "w")
file=open("demo.txt", "r")
#file=open("demo.txt", "a")
#file=open("demo.txt", "r")
#file mood w=write,a=append,r=read, if new file mood=x
#file.write("I love Python\n")
#file.write("I love Javascript Also\n")
#reading=file.read()
#file.write(" and Networking")
#reading=file.read()
#print(reading)
#for print multilien use readline()
frist_line=file.readline()
second_line=file.readline()
print(frist_line)
print(second_line)
file.close()
#os.remove("demo.txt) it will be outside of open close
#for open a file
#files=open("c:user/desktop/demo.txt","r")
#x=files.read()
#print(x)
#file.close()
