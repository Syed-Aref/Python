
#1
"""
class Employee :
    pass
emp1 = Employee()
"""

#2
"""
class Employee :
    def __init__(self) :
         print("An object has been created")

emp1 = Employee() 
#Outputs : An object has been created
"""

#3
'''
#Variable naming:same name as arguement in class-->Possible
class Employee :
    def __init__(self,name1,name) :
        self.name1 = name1
        self.name = name
        
        print("An object has been created")
        print("name :  ",self.name)
        print("name1 : ",self.name1)
        #printing memory
        print(self)


emp1 = Employee("Aref","Ahmed") 
print(emp1.n)
print(emp1) # This prints memory



'''


#4
'''
#Variable naming:same name as arguement in class with crossing-->Possible
class Employee :
    def __init__(self,name,name1) :
        self.name1 = name
        self.name = name1
        
        print("An object has been created")
        print("name :  ",self.name)
        print("name1 : ",self.name1)
        #printing memory
        print(self)

emp1 = Employee("Aref","Ahmed") 
print(emp1.name)
print(emp1) # This prints memory

'''

'''
#5
#Variable naming: Different variable name in class --> Possible
class Employee :
    def __init__(self,name,name1) :
        self.name1 = name1
        self.n = name
        
        print("An object has been created")
        print("name1 : ",self.name1)
        #printing memory
        print(self)
    def print_n(self) :
        print("n : ",self.n)

emp1 = Employee("Aref","Ahmed") 
print(emp1.n)
print(emp1) # This prints memory
emp1.print_n()
'''

#6
'''
class house :
    def __init__(self) :
        # bt default values
        self.windows = 5
        self.doors  = 1
        
    def view_h(self) :
        print("windows : ",self.windows)
        print("doors : ",self.doors)



h1 = house()
h2 = house()

h1.view_h()
h2.view_h()

'''

#7
'''
class Employee :
    def __init__(self,name1,name) :
        self.name1 = name1
        self.n = name
        self.digit = 0
        print("An object has been created")
        print("n :  ",self.n)
        print("name1 : ",self.name1)
        #printing memory
        print(self)
    def set_digit(self,n) :
        if (type(n) is int)==False :
            print("Error")
        else :
            self.digit = n

emp1 = Employee("Aref","Ahmed") 
print(emp1.n)
print(emp1) # This prints memory
'''






class A :
    def meth_a(self,n) :
        A.n = n
        return A.n*10

a = A()
print( a.meth_a(5) )























