# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 23:19:11 2020

@author: User
"""

'''
class sum:

    def __init__(self, x, y):

        self.num = x + y

num1 = sum(10, 20)

num2 = sum(20, 30)

# print(num1+num2) --> Error

n1 = 5
n2 = 7

print(n1+n2)
print(n1.__add__(n2))

# This works for string + string as well

# What if we use'+' or '-' for class data type
# This is called method overloading

class num :
    def __init__(self,x) :
        self.val = x
        
    def __add__(self,other) :
        return self.val + other.val
    
    def __gt__(self,obj) :
        if self.val > obj.val :
            return True
        else:
            return False
    def __lt__(self,obj) :
        if self.val < obj.val :
            return True
        else:
            return False


num1 = num(78)
num2 = num(2)
print(num1+num2)

num3 = num1+num2
print( type(num3) )
'''

'''
#Enacpsulation   
class AccountsC09 :
    def __init__(self):
        self.name = "abc"
        self.no = 1234
        self.bln = 0.0

        self.__gen = "m"

    def printgen(self):
        print(self.__gen)
    def __printgen(self):
        print(self.__gen)

    def retgen(self):
        return self.__gen + "i"

a1 = AccountsC09()
print(a1.name)
#print( a1.__gen )
a1.printgen()
#a1.__printgen()

a1._AccountsC09__printgen()
print( a1._AccountsC09__gen )

print( a1.retgen() )

class ABC :
    def __init__(self) :
        self.obj = AccountsC09()
        self.x = -10
    def printInfo(self):
        print(self.obj.bln)

abc = ABC()

def name():
    return None
'''

'''
#Initializing variable
class X:
    def __init__(self) :
        self.x1 = 0
    def func(self) :
        self.x2 = -1


x = X()
#print(x.x2) -> Error. First we will have to initialize it
x.func()
print( x.x2 )
'''

'''
# static var example -1
class Player :
    
    tm_rn = 0
    def __init__(self) :
        self.rn = 0
        
    def hit_four(self) :
        self.rn += 4
        Player.tm_rn += 4
    def hit_six(self) :
        self.rn += 6
        Player.tm_rn += 6
        
tamim = Player()
sakib = Player()

tamim.hit_four()
sakib.hit_six()


print( tamim.rn )
print( sakib.rn )
print( Player.tm_rn )
'''

'''
# static var ex-2
class student :
    cnt = 0
    def __init__(self,name,id) :
        self.nm = name
        self.id = id
        student.cnt += 1
    def details(self) :
        print("Name:",self.nm)
        print("ID:",self.id)
    
    
    
s1 = student("bob",10)
s2 = student("alice",13)

s1.details()

print( student.cnt )
print( s1.cnt )

'''







# constructor overloading
class student :
    cnt = 0
    def __init__(self,name,id) :
        self.nm = name
        self.id = id
        student.cnt += 1
    def details(self) :
        print("Name:",self.nm)
        print("ID:",self.id)

    @classmethod
    def from_str(cls,info):
        name,id = info.split("-")
        obj = student(name,id)
        #obj = cls(name,id) --> also correct
        return obj
    @classmethod
    def print_uni(cls) :
        print("bracu")

s1 = student("bob",10)
s2 = student.from_str("alice-13")
s1.details()
s2.details()

s1.print_uni()


student.print_uni()
