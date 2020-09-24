# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:55:58 2020

@author: User
"""


def func(*s) :
    print("My car is",s[0])
    print("My phone is",s[1])
func("Toyota","Apple")    
#func("Toyota") --> Error
'''
Output:
My car is  Toyota
My phone is  Apple    
'''


#Similar type
def func01(*s) :
    print("My name is",s[0])
    print("My age is",s[1])
func01("Aref",20)
func01("Aref","Twenty")
'''
Output:
My name is Aref
My age is 20
My name is Aref
My age is Twenty
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