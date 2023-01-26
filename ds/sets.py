#Initialzie set
set1 = set()

set1.add(1)
set1.add(2)
set1.add(3)
set1.add(4)
set1.add(5)
set1.add(9)

#Print set
print(set1)

#No duplicte elemensts
set1.add(2)
print(set1)

#Eleemnts in set
print(1 in set1)
print(30 in set1)
print(1 not in set1)
print(30 not in set1)

#Removineg an elmnent that exists in set
set1.discard(2)
print(set1)

#Removineg an elmnent that does not that exists in set
set1.discard(20)
print(set1)

#sets are ordered
set2 = set()
for i in range(0,10,2):
    set2.add(i)
print(set2)
for i in range(1,10,2):
    set2.add(i)
print(set2)
