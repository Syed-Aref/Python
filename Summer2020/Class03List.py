# Empty list
empty_list = []


##Inserting
#(1)
lst = []
lst.append(90)
lst.append(90)
lst[0] = 23
# lst[2] = 89 --> wrong statement;can not assign values in this way
lst.append(89)
print(lst[0])
#(2)
'''
lst.insert(index,value)
index >= 0 & index<=len(lst)
0 --> inserts as 1st element
1 --> inserts as 2nd element
... ... ... ... ... ... ... ... 
... ... ... ... ... ... ... ... 
len(lst) --> inserts as last element
'''


#List of single type element
list1 = [2,3,5,7]

#List of multiple type element
list2 = [1,34,3.5,"o"]

#List initializing by constructor
list3 = list([6,7,8])

#printing list
print(list3) #Entire list3 will printed.Output : [6,7,8]

#Indexing : same as string

#Accessing elements : same as java array
print(list1[2]) #Accessing  3rd element (0 based indexing have been used)

#Mutanbility of list
list1[2] = 15
print(list1[2]) #15 will be printed, not 5

#Removing element/list
del list3[1] # list3 = [6,8]
del list3 #list3 will be cleared from memory.We can not access list3 unless initializing it again
list1.clear() #All elements form list1 will be cleared but not be deleted from memory.list1 = []


#List input
s = "a,b,78"
l2 = []
l2  = s.split(",")
for i in l2 :
    print( type(i) )
print(l2)


s_t = l2[2]
s_num = int(s_t)
l2[2] = s_num
for i in l2 :
    print( type(i) )
print(l2)
