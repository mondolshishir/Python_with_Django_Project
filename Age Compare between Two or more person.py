name1=input("Enter The name of frist friend: "  )
name2=input("Enter The name of Second friend: " )
age1=input("Enter The age of " +name1+ ":")
age2=input("Enter The age of " +name2+ ":")

if age1>age2:
    print( name1+ " is Bigger Than "+name2 )
elif age1<age2:
    print(name2 + " is Bigger Than " + name1 )
else:
    print(name1+ " and " +name2+ " are the Same Age")


