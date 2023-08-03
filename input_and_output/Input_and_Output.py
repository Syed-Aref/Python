s1 = input() #takes input as String
print(s1)
print(type(s1)) # type of s1 = str

s2 = input("Enter num : ")
print(s2)
print( type(s2) ) # type of s2 = str
# In console "Enter num : " message will be shown in first line.Then on the next line it will take input.

num = int(s2) #Converts String s2 to num
print(num)
print(num*10)

print(s1,s2,num*2,"iii") 
#Output:
#s1 s2 num*2 iii
print(s1,s2,num*2,"iii",sep=" - ")
#Output:
#s1 - s2 - num*2 - iii

print("Dhaka is a big city.")
print("Dhaka is caapital of BD.")
#Output:
#Dhaka is a big city.
#Dhaka is caapital of BD.
print("Dhaka is a big city.",end="")
print("Dhaka is caapital of BD.")
#Output:
#Dhaka is a big city.Dhaka is caapital of BD.