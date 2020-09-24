# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:21:49 2020

@author: User
"""

# In Dictionary : 
'''
1.Keys will be immutable data type(string,int,float)
2.Values willl be both immutable+mutabke data type(string,int,float,list,dictionary)
3. dictionary = {k1:v1,k2:v2,k3:v3, .... ,kn:vn}
k1 != k2 !=.....!=kn
v1 = v2 =.....=vn
4.In a list both keys and values have no restrictions(Any key or value can be used)
'''

#Initializing dictionary
my_dic1 = {1:'a',2:'b'};
my_dic2 = {1:'a','A':'b'};
my_dic3 = {1:'a',2:2}
my_dic3 = {1:[1,2,3],"abc":2};
my_family ={
    "lst" : [1,2,3,4],
    "child" : {"c1" : "a","c2" : "b"}
    } #Exemple of nested dictionary
my_dic4 = {} #OP : {}

#printing dictionary
print(my_dic1) #OP : {1: 'a', 2: 'b'}
print(my_dic4)

#printing dictionary key values
print(my_dic1.get(2)) #OP : b  [value of key 2]
print(my_dic3.get(1)[2]) #OP : 3 [ key 1 is [1,2,3,4].So, list key 1[2] is 3 ]

# Adding Elements in dictionary
my_dic2[2] = "i"
print(my_dic2[2]) #OP : i
print(my_dic2) #OP : {1: 'a', 'A': 'b', 2: 'i'}. 2:'i' has been added
print(my_dic2.pop(2)) #OP : i.
print(my_dic2) #OP : {1: 'a', 'A': 'b'}. 2:'i' has been deleted


# loop in dictionary
for i in my_dic3 :
    print(i," = ",my_dic3[i])
for i,j in my_dic3.items() :
    print(i," = ",j)
    
#Cheking if key is present in dictionary or not.(Return type is boolean)   
print(4  in my_dic3) #Will chehck if key 4 is present in dictionry.

#item pair , keys and values
print(my_dic1.items()) #OP : dict_items([(1, 'a'), (2, 'b')])
print(my_dic1.keys()) #OP : dict_keys([1, 2])
print(my_dic1.values()) #OP : dict_values(['a', 'b'])

#Builing dictionary
dic = {}
dic = dic.fromkeys([4,2,3],"A")
print(dic) #OP : {4: 'A', 2: 'A', 3: 'A'}

#list of keys
print( list(dic.keys()) )

#list of values
print( list(dic.values()) )

# list of keys in sorted order[Returns list of keys in sorted order]
print( list( sorted( dic.keys() ) ) ) #OP : [2, 3, 4]






# soring by value
import operator
d= {1:2,2:2,4:1,56:30,23:14}

ascening_sorted_d = dict( sorted( d.items(),key=operator.itemgetter(1) ) )
print(ascening_sorted_d)

descening_sorted_d = dict( sorted( d.items(),key=operator.itemgetter(1) ,reverse=True) )
print(descening_sorted_d)

#concatening in dictionar
d1 = {1:2,3:4}
d2 = {'a':'A'}
d3 = {}
for d in (d1,d2) : d3.update(d)
print(d3) #OP : {1: 2, 3: 4, 'a': 'A'}

d1 = {1:2,3:4}
d2 = {'a':'A',3:6}
d3 = {}
for d in (d1,d2) : d3.update(d)
print(d3) #OP : {1: 2, 3: 6, 'a': 'A'}.So always takes the value of last key

d_merge = {**d1,**d2}
print(d_merge) #OP : {1: 2, 3: 6, 'a': 'A'}

# creating dictionry from list of keys and values
keys = [1,2,3]
values = ['a','b','c']
d = dict(zip(keys,values))
print(d) #OP : {1: 'a', 2: 'b', 3 : 'c'}

keys = [1,2,3]
values = ['a','b']
d = dict(zip(keys,values))
print(d) #OP : {1: 'a', 2: 'b'}

keys = [1,2,2]
values = ['a','b','c']
d = dict(zip(keys,values))
print(d) #OP : {1: 'a', 2: 'c'}

#minimum key 
d = {'Physics':1,'CS':3,'CSE':2}
L = d.keys() #Mking a list of keys
print(min(L))

#CREATING NEW DICTIONARY FOLLOWING KEYS FROM GIVEN DICTIONARY
d= {1:'a',2:'b',3:'c',4:'d'}
keys = [1,3]
new_d = { k : d[k] for k in keys}
print(new_d)

