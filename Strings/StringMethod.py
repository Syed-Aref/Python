##Methods:
# 1.upper caseing
s = "rrt"
print(s.upper())

# 2.lower casing
s = "eE"
print(s.lower())

# 3.length
string = "Aref graduated"
len(string)

# 4.count(string_var)
str = "hi friend hi"
print(str.count("hi"))
#Output: 2

# 5.count(string_var,from,to)
str = "hi friend hi"
print(str.count("hi", 0, 11))
#Output: 1
# [from,to)
# min value of to : from+1(unless it will not work)

# 6.startswith(str_var)
str = "hi friend hi"
print(str.startswith("hi"))
#Output: True

# 7.startswith(str_var,from,to)
str = "hi friend hi"
print(str.startswith("fr", 3, 4))
#Output: False

# 8.endswith(str_var)
str = "hi friend hi"
print(str.endswith("hi"))
#Output: True


# 9.endswith(str_var,from,to)
print(str.endswith("hi", 0, 10))
#Output: False

# 10.find(str_var)
str = "Hi friend hi friend"
print(str.find("hi"))
#Output: 10
# Returns first occurance

# 11.replace(replacing_str,replaced_by_str)
str = "Hi friend hi friend hi"
print(str.replace("hi", "bye"))
#Output: Hi friend bye friend bye
#Replaces all replacing_st strings

# 12.replace(replacing_str,replaced_by_str,n)
str = "Hi friend hi friend hi"
print(str.replace("hi", "bye", 1))
#Output: Hi friend bye friend hi
#Replaces first n replacing_st strings

#SLICING
sliced_s = s[2:6:1]
# sliced s = s[2]s[3]s[4]s[5]
"""
sliced_s = s[from:to:step]
(*)to>=from+1
(*)step>0 or step<0
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
from or to, then the function automatically works by 
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
'''