from functools import reduce
li = [1,2,3,4,5]
def fun1(x, y):
    return x + y
sum = reduce(lambda x, y:x+y, li)
print(sum)