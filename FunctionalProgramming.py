

""" Functions as first-class objects(as variable) """
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def calc(f,a,b):
    return f(a,b)

print( calc(add,6,5) )
print( calc(sub,6,5) )


""" Higher level functions """
#map : gives list of returned values
def cube(x):
    return x*x*x

list1 = map(cube,[1,2,3,4])

for i in list1:
    print(i , end=" ")
print()

#lambda function : anonymous function
square = lambda x :  x*x
print(square(10))

anonymous_print = lambda x :  print(x)
anonymous_print("Aref")

anonymous_print = lambda x :  print(x,"--> has been printed")
anonymous_print("Aref")
