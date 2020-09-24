'''
-->Types:
      a) void
      b) return
// same as java or other languages

-->Function body:
def myFunc(n) : 
    // .. function body ..
    // ...................
Here, n can be string,integer or any data type
Similarly, for multiple constructors as myFunc(n1,n2,n3) n1,n2,n3 can be any data type
'''
def func(n) :
    print("My age is",n)



## -->Default argument
def myFunc(name , age = 1) : 
    print("Name of this kid : ",name)
    print("Age of this kid : ",age)
myFunc("Hasan")  
print("---------------------")
myFunc("Ahmed",5)
print("---------------------")
myFunc("Anam","Five")
print("---------------------")
myFunc(age = '10',name = "Shaad")

##-->Fixing argumenst
def func01(n1,n2) : 
    return 1*n1+2*n2;
print( func01(2,1) )
print( func01(n2=2,n1=1) )
'''
Output:
4
5
'''
def func02(s1,s2,s3,s4):
    print("s1 = ",s1)
    print("s2 = ",s2)
    print("s3 = ",s3)
    print("s4 = ",s4)
func02(10,12,14,16)
'''
Outout:
    s1 = 10
    s2 = 12
    s3 = 14
    s4 = 16
'''    
func02(s4 = 16,s2 = 12,s1 = 10,s3 = 14)
'''
Outout:
    s1 = 10
    s2 = 12
    s3 = 14
    s4 = 16
'''   
def squareFunc(x, y = 0):
    return (x*x + 2*x*y + y*y)
print( squareFunc(5,2) ) # (5+2)^2 = 49
print( squareFunc(5) ) # (5+0)^2 = 25.Since default value for y is set 0.
# func(not default+defalut)

##-->Multiple number of argument in parameter
def func03(*s) :
    print("My car is",s[0])
    print("My phone is",s[1])
func03("Toyota","Apple")    
#func("Toyota") --> Error
'''
Output:
My car is  Toyota
My phone is  Apple    
'''
def func04(*s) :
    print("My name is",s[0])
    print("My age is",s[1])
func04("Aref",20)
func04("Aref","Twenty")
'''
Output:
My name is Aref
My age is 20
My name is Aref
My age is Twenty
'''
##-->Multiple number of arguments+default argument
def myFunc_(*args,val) :
    return args[0]*args[1]*val
print( myFunc_(10,50,val = 60) )
print( myFunc_(10,50,55,val = 60) )
'''
Output:
30000
30000
'''



print( (lambda x, y,z: (x + y+z)*(x+y+z)) (4,3,5) )
'''
Lambda func structure
(lambda  ...arguments... : (..calculation..)) (..given args..)
'''
def empty01() :
    pass
def empty02(s) :
    pass
def empty03(*s) :
    pass

empty01()
empty02(12)
empty02("Twelve")
empty03()
empty03(12,"Twelve")
'''
pass means doing nothing 
'''
