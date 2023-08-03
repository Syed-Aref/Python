

# Repetition of string in line
s = "I am Baymax"
print(s * 4) 
"""
Outout:
I am BaymaxI am BaymaxI am BaymaxI am Baymax    
"""


# Repetition of string(one in each line)
s1 = s + "\n"
print(s1 * 4) 

# Repetition of string in line with gap in between
s1 = s + " "
print(s1 * 4) 
#Also
print(s,end = "")
s1 = " " +s
print(s1*(4-1))

#SLICING
sliced_s = s[2:6:1]
# sliced s = s[2]s[3]s[4]s[5]
"""
sliced_s = s[from:to:step]
to>=from+1
step>0 or step<0

By default:
(*)If from,to and all are vacant
from = 0,to = n-1(n = string length),step = 1
(*)If only setp is given :
    If step>0;from = 0,to = n-1
    If step<0,from = -n, to = 0
"""
s1 = s[-9::]
print(s1)
'''
If in sliced function,(-)value has been set for 
from or to, then the function auto,atically works by 
negetive indexing
'''
#Formatting:


#String
s = "Hello {}.Today is Sunday".format("Alice")
print(s)
'''
print( "Hello {}.Today is Sunday".format("Alice") ) --> is also applicable
'''
s = "Hello {0}.Today is {1}".format("Alice","Sunday")
print(s)
s = "Hello {1}.Today is {0}".format("Monday","Alice")
print(s)
'''
These coulde be also printed as:
print( "Hello {0}.Today is {1}".format("Alice","Sunday") )
print( "Hello {1}.Today is {0}".format("Monday","Alice") )
'''


#Number
s = "Hello.He is{0:d}".format(12)
print(s)


#Number+String
s = "Hello {0}.It is {1:d} pm".format("Aref",11)
print(s)
'''
print( "Hello {0}.It is {1:d} pm".format("Aref",11) ) --> is also applicable
'''


# Number allingnment
print("{0:>5d}".format(56))
'''
OUTPOUT:
   56
Exp:
Only >5 is inserter after [0:] and before [d].
>5 means takes 5 positions(boxes) and prints from backward
<5 means takes 5 positions(boxes) and prints from forward
'''
print( "{0:>7d} is my birth year.I am{1:<7d} is years old".format(2000,20) )
print( "{0} is hot.{1:f} is todays temperature".format("Today",40.56893) )
"""
Output:
Today is hot.40.568930 is todays temperature
#Took all floating points also added one trailing zero
"""
print( "{0} is hot.{1:.3f} is todays temperature".format("Today",40.56893) )
"""
Output:
Today is hot.40.569 is todays temperature
#Took only 3 floating points
"""

"""
str = "HeLLo FrIeNDs"
print(str.lower()) #hello friends

str = "HeLLo FrIeNDs"
print(str.upper()) #HELLO FRIENDS

str = "hi friend hi"
print(str.count("hi")) #2

str = "hi friend hi"
print(str.count("hi", 0, 11)) #1

str = "hi friend hi"
print(str.startswith("hi")) #boolean
str = "hi friend hi"
print(str.startswith("fr", 3, 4)) #boolean

str = "hi friend hi"
print(str.endswith("hi")) #boolean
str = "hi friend hi"
print(str.endswith("hi", 0, 10)) #boolean

str = "Hi friend hi friend"
print(str.find("hi")) #returs first occuring position if string inside parameter is present,else returns -1


str = "Hi friend hi friend hi"
print(str.replace("hi", "bye")) #Hi friend bye friend bye

str = "Hi friend hi friend hi"
print(str.replace("hi", "bye", 1)) #Hi friend bye friend hi(Replaces first occurance)

"""














