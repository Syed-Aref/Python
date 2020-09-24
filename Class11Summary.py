# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 18:27:02 2020

@author: User
"""


'''

(*) No object for an abstract class(cant be created)



'''

from abc import ABC, abstractmethod

# we want ans abstract class 'A'
class A(ABC) :
    
    '''
    def meth_a(self) :
        print("meth_a")
    '''
    @abstractmethod
    def meth1(self) :
        pass  
    

# a = A() --> Error.A is an abstract class
#Even if we uncomment meth_a, A will be still abstract class 
# The only way to make A concrete is t remove @abstractmethod from line 26
'''
class B(A) :
    
    def meth2(self) :
        print("meth2")

# b = B() --> Error
# abstract meth_1 is not over-riden
'''



'''
class B(A) :
    
    def meth1(self) :
        print("meth1 over-riden")
    
    def meth2(self) :
        print("meth2")

b = B()    # this works      
'''  
        
   
'''
class B(A) :
    
    def meth_1(self) :
        print("meth1 over-riden")
    @abstractmethod
    def meth2(self) :
        print("meth2")     
#b = B() --> will give error because B stillhas an abstract method        
'''


'''
class B(A) :
    @abstractmethod
    def meth2(self) :
        print("meth2")  
class C(B) :
    def meth3(self) :
        print("meth3")
# c = C() will give error as C is also an abstract mehtof
# C has two abst. methods. meth1 from A and meth2 From B
# In order to make C concrete we need to override both meth1 and meth2
'''






''' -------------------------------------------------------------------- '''

'''
class Animal(ABC) :
    @abstractmethod
    def make_sound(self) :
        pass
    def eat(self) :
        print("I am eating")
class Dog(Animal) :
    def make_sound(self) :
        print("dog barking")

class Cat(Animal) :
    def make_sound(self) :
        print("meow")   
d1 = Dog()
c1 = Cat()
d1.make_sound()
c1.make_sound()
# calling concrete methods
d1.eat()
c1.eat()
'''


'''
class Animal(ABC) :
    @abstractmethod
    def make_sound(self) :
        print("A")
    def eat(self) :
        print("I am eating")
class Dog(Animal) :
    def make_sound(self) :
        super().make_sound()
        print("dog barking")

d1 = Dog()
d1.make_sound()
# We can see that abstract method from Animal is working.But it should not be used.Because abstract methods should not do anything   
'''









































      
        
        
        
        
        
