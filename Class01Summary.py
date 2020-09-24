# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:25:12 2020

@author: User
"""
print("IOP","TI",sep = " ")
print("IOP","TI",sep = " ")
'''
Out:
IOP TI
IOP TI    
'''
print("") # A line gap
print("IOP","TI",sep = " ",end = "")
print("<gap>","IOP","TI",sep = " ")
print("IOP","TI",sep = " ")
'''
Out:
IOP TI<gap>IOP TI 
IOP TI    
'''

"""
5/2 = 2.5
5//2 = 2
"""

if "S" in "ss" :
    print(True)
else :
    print(False)
    
if "s" in "ss" :
    print(True)
else :
    print(False)    
'''
False
True
''' 

'''

For else if, python has : elif
For else, python has : else
For or operation,python has : or
For and operation,python has : and

'''

for i in "Hello" :
    print(i)
'''
H
e
l
l
o
'''    
# Print and check data type
s=90
print( type(s) )
str_ = "m"
print( type(str_) )
print( type(str_) is str )
print( type(str_) is int )


#Base transformation
#int(num,b) can change any num of b to its corresponding integer(decimal) value

#Binary to decimal
s_bin = "101011"
n = int(s_bin,2)
print(n)

#Octal to decimal
s_oct = "1010300607"
n = int(s_oct,8)
print(n)
