#Initialzie set
set1 = set()

set1.add(1)
set1.add(2)
set1.add(3)
set1.add(4)
set1.add(5)
set1.add(9)

#Print sets
print(set1)

#Nop duplicte elemensts
set1.add(2)
print(set1)

#Eleemnts in set
print(1 in set1)
print(30 in set1)
print(1 not in set1)
print(30 not in set1)

#Removineg elmnent that exists in set
set1.discard(2)
print(set1)

#Removineg does not that exists in set
set1.discard(20)
print(set1)

#sets are unordered
import random
import math

set2 = set()

for i in range(10):
    set2.add(math.floor(random.random()*100))
print(set2)
