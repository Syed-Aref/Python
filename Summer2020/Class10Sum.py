'''
Base class,parent class,super class
Subclass,derived class,child class

subclass inherits properties from super class
subclass "is a" relation with super class

child classes inherit all properties from parent class
but parent classes donot inherit from child class

         |-> child1
         |-> child2
parent---|-> child3
         |-> chld4

But, child1 -> parent is not possible
Similarly, child2 -> parent is not possile

EX:

class BaseClass :
    --------
    --------
class DerivedClass(BaseClass) :
    --------
    --------

Method resolution order : searches int its own class.If not found 
searches in parent class

Single inheritence :
parent class-->child clas

Multilevel :
parent class -- > child1 --> child2

child1 inherits all properties from parent class
child2 inherits all properties from child1 and parent class

Hierarchical :
      parent class
        /    \    
       /      \
      child1   child2
Hybrid:
    
           
          
       parent class    
           ^
           |
       child1 class
        /    \    
       /      \
      child1   child2 

super() --> used to call methods from parents class


Method override :
    If a amethod is present in both parent and child class,
    method overriding allows to use method in child class
'''

'''
#Single
class Animal :
    def __init__(self,name) :
        self.name = name
    def meth1(self) :
        print(self.name ,"is in meth1")

class Dog(Animal) :
    
    def bark(self) :
        print( self.name,"is barking!" )
    def meth1(self) :
        print(self.name,"is in meth1")
a1 = Animal("Jack")
d1 = Dog("Rover")
d1.bark()
a1.meth1()
d1.meth1()
# isinstance(obj_name,class_name) #is obj_name instance of class_name
# issubclass(obj_name,class_name) #is obj_name subclass of class_name
'''

'''
#Hierarchical
class Student :
    def __init__(self,n,i) :
        self.name = n
        self.id = i
    def details_(self) :
        print("Name:",self.name)
        print("Id:",self.id)

class CSEStudent(Student) :
    def __init__(self,n,i,l) :
        super().__init__(n,i) 
        self.labs = l
    def do_lab(self) :
        print(self.name,"is doing lab")


class BBAStudent(Student) :
    
    def chill(self) :
        print(self.name,"is chilling")


s1 = CSEStudent("Bob",11,3)
s2 = BBAStudent("Carol",36)
print( help(s1) )
'''

'''
#Multilevel
class Student :
    def __init__(self,n,i) :
        self.name = n
        self.id = i
    def details_(self) :
        print("Name:",self.name)
        print("Id:",self.id)

class CSEStudent(Student) :
    def __init__(self,n,i,l) :
        super().__init__(n,i) 
        self.labs = l
    def do_lab(self) :
        print(self.name,"is doing lab")



class CSEFresher(CSEStudent) :
    
    def enroll_(self) :
        print(self.name," enrolled in CSE110")

s1 = CSEStudent("Bob", 11, 3)
s2 = CSEFresher("Carroll", 11, 3)
'''

'''
# Variable overriding
class Animal :
    def __init__(self,name) :
        self.name = name
        self.color = "White"


class Dog(Animal) :
    
    def __init__(self,n,c) :
        super.__init__(n)
        self.color = c
    
    def bark(self) :
        print(self.name," is barking !")
'''

'''
#Method overriding
class A :
    def __init__(self,n) :
        self.n = n
    def meth1(self) :
        print(self.n,"is studying in meth1")

class B(A) :
    
    def meth1(self) :
        print(self.n," is partying in meth1")
        super().meth1()



a1 = A("A1")

b1 = B("B1")

a1.meth1()
b1.meth1()
'''




'''
# __str()__

class Student:
    def __init__(self,n,id) :
        self.name = n
        self.id = id
        print("Name:",self.name)
        print("Id:",self.id)
        print( self )
        
        
    def __str__(self) :
        s = self.name + "kkk"
        return s

s1 = Student("bb",11)


print( s1 )
print( s1.__str__() )
'''


class Animal :
    def __init__(self) :
        self.name = "5"
        self.color = "White"


class Dog(Animal) :
    
    def __init__(self,n,c) :
        self.name2 = n
        self.color = c
    
    def bark(self) :
        print(self.name," is barking !")





d1 = Dog()
print( d1.name )