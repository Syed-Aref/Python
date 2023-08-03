nmax = 10 + 5
inf = 1000000
mat = [ [] for i in range(nmax) ]

print("mat=>")
for i in mat : 
    print(i)
print("---------------------------")

for i in mat : 
    for j in range(3) :
        i.append(j)

print("mat=>")
for i in mat : 
    print(i)
print("---------------------------")

print( "mat[" , 8 ,"][" ,1, "] : " , mat[8][1])

mat[8].append(3)

for i in mat : 
    print(i)
print("---------------------------")

mat1 = []

for i in range(5):
    mat1.append([])

print("mat1=>")
for i in mat1 : 
    print(i)
print("---------------------------")



for i in range(5):
    mat1[i].append(1)
    
print("mat1=>")
for i in mat1 : 
    print(i)
print("---------------------------")




for i in mat1:
    for j in range(2,5+1,1) :
        i.append(j)

print("mat1=>")
for i in mat1 : 
    print(i)
print("---------------------------")

print( "mat1[",2,"][",3,"] : ",mat1[2][3] )
