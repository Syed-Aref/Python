# Print "Hello world" 5 times.
count=1
while count<=5:
   print("Hello World")
   count = count + 1
# -------------------------

# Infinite loop:
count = 5
while True:
  print(count)
  count+=1
# -------------------------

# break:
count = 1
while True:
  print(count,end=" " )
  count = count+1
  if count == 5:
    break
# ------------------------- 

# continue:
count = 0
while count<5:
  count+=1
  if count==3:
    continue
  print("Hello",count)    
  
# ------------------------- 

# Nested loop
outer = 1
while outer <=2:
  inner = 1
  while inner <=3:
    print(outer,",",inner)
    inner+=1
  print ("Inner loop terminates.")
  outer+=1
print ("Outer loop terminates.")  
# ------------------------- 

# For in python:
for i in range (1,10,2):
    print(i)

# Similar loop in java
# for (int i=1;i<=9;i=i+2)  // i<=9 is same as i<10
# {
#     System.out.println(i);
# }

# More ex:
for i in range(5):
    print(i)
# By default it sets i = 0, holds condition i<5 and increment by 1

# String
for i in "Hello":
    print(i)
# ------------------------- 
# indentation rule: same as if/elif/else