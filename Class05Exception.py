





'''
a = 3
b = 0

try :
print(a/b)
expect Exception as e:
    print("Error occured")
    print(e)


print("bye")

'''


'''
#Inputing error
try :
    a = int(input())
    b = int(input())
    print(a/b)
expect Exception as e : 
    print(e)    
print("Bye")
'''


#Types of error :
try :
    a = int(input())
    b = int(input())
    print(a/b)
except ZeroDivisionError as z :
    print("Category 1  : ",z)
except ValueError as v :
    print("Category 2 : ",v)  
except Exception as e :
    print(e)


 #finally 
try :
    a = int(input())
    b = int(input())
    print(a/b)
except ZeroDivisionError as z :
    print("Category 1  : ",z)
except ValueError as v :
    print("Category 2 : ",v)  
except Exception as e :
    print(e)

finally :
    print("done")

'''
Note : finally can be implemented only after try-except
Q : Whats the difference between code in 'finally' or code in normal?
A : If we use finally after try and exception, even if the code causes 
runtime error the function/code inside finally keyword still works.
'''


















        