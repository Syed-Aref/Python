

# Pass by reference
'''
class   Person :
    def __init__ (self,name,age) :
        self.name = name
        self.age = age
        
    def view(self) :
        print("Name : ",self.name," \nAge : ",self.age)

    def compare_age(self,p): # Reference of object p passed here
        if(p.age==self.age):
            print("Same age")
        else:
            print("not same age")
        
p1 = Person("Aref",21) 
p2 = Person("Hasan",21)

p1.view()
p2.view()
p1.compare_age(p2)
'''

# Call by reference and value : comparison
'''
class   Person :
    def __init__ (self,name,age) :
        self.name = name
        self.age = age
        
    def view(self) :
        print("Name : ",self.name," \nAge : ",self.age)

    def compare_age(self,p):
        if(p.age==self.age):
            print("Same age")
        else:
            print("not same age")
    def func(self,num,NAMES) : #Value of num and object of names called/passed here
        num = num+5
        nm = NAMES
        nm[0] = "Yasin" 
        print("Inside Method: ",num)
        print("Inside Method: ",nm)
p1 = Person("Aref",21) 
p2 = Person("Hasan",21)

p1.view()
p2.view()
p1.compare_age(p2)



x = 34
names = ["Ahmed","Khan"]

p1.func(x,names) 
print("Outside Method: ",x)
print("Outside Method: ",names)
# Would also work without creating nm object.( names[0] = "Yasin" )  
'''


# Class in method(parameter and returning)
'''
class   Person :
    def __init__ (self,name,age) :
        self.name = name
        self.age = age
        
    def view(self) :
        print("Name : ",self.name," \nAge : ",self.age)

def get_instance() :
    return Person("Amin",30)   

def call_instance(instance) :
    instance.view()        
p1 = Person("Aref",21) 
p2 = Person("Hasan",21)

p1.view()
p2.view()


p3 = get_instance()
p3.view()
call_instance(p3)
'''

#None
'''
class   Student :
    def __init__ (self,name="x") :
        self.name = name
        self.id = None #None is a keyword
s1 = Student("Hossain")  
print(s1.id)      


s2 = Student()
print(s2.name)
print(s2.id)
'''

# Method Overloading
'''
class Calculator:
    # Using none(return)
    #'' '
    def func(self,num1,num2,num3=None) :
        if num3 == None :
            return num1 + num2
        else :
            return num1*num2*num3
    #'' '
    # Using tuple(return)
    #'' '
    def func(self,*n) :
        if len(n)==2 :
            return n[0]+n[1]
        elif len(n)==3 :
            return n[0]*n[1]*n[2]
    #'' '
    # Using tuple(print)
    def func(self,*n) :
        if len(n)==2 :
            print ( n[0]+n[1] )
        elif len(n)==3 :
            print ( n[0]*n[1]*n[2] ) 

  
c1 = Calculator()
# None(return)
#'' '
print( c1.func(5,10) )
print( c1.func(5,10,5) )
#'' '
# Tuple(return)
#'' '
print( c1.func(5,10) )
print( c1.func(5,10,5) )
print( c1.func(5) )
#'' '
# Tuple(print)
c1.func(5,10) 
c1.func(5,10,5) 
c1.func(5)

'''

# Constructor overloading
'''
class Student :
    def __init__(self,name,id,cg=None) :
        self.name = name
        self.id = id
        #self.cg = 0.0
        if cg!=None :
            self.cg = cg
        

s1 = Student("Aref",12)
s2 = Student("Aref",12,4.5)
'''
#Using tuple(same as previous)

#Also we can use dictionary

class Student :
    def __init__(self,**info) :
        if len(info)==2 :
            self.name = info['name']
            self.id = info['id']
        elif len(info)==1 :
            self.name = info['name_']

s1 = Student(name = "Khan",id = 56)
s2 = Student(name_ = "Kalam")
























