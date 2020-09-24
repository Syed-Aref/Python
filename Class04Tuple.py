
#inititlizing tuple
tup1 = (2,4,5)
print(tup1) #OP = (2, 4, 5)

#accessing
print( tup1[2] ) #5 [3rd element;as tuple has 0-based indexing]

#empty tupl
emp_tupl = ()
print(emp_tupl)

# packing
tuple_1 = (1,2,"a")

# unpacking
a,b,c = tuple_1
print(a) #OP : 1
print(b) #OP : 2
print(c) #OP : a

# tuple items can not be changed
'''
tup1[1] = 8 -->Error
'''

# elements of a list inside tuple can be changed(But the whole list object can not be changed/removed)
tup = (1,[2,3,5])
print(tup[1][1])
tup[1][1] = 10
print(tup[1][1])
tup[1].clear()
print(tup)
#tup[1] = [] --> Wrong
#tup[1] = [1,2] --> Wrong
#tup[1] = "List" --> Wrong

#Concatenation
tup1 = (1,2,3)
tup2 = (4,5,6)
tup3 = tup1 + tup2
print(tup3) #OP : (1, 2, 3, 4, 5, 6)
tup4 = (4,5,6,7,8)
tup5 = tup3+tup4
print(tup5) #OP : (1, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8)

# tuples allow duplcate elements
