# We will implement st ad queue data structure using Collections.deque()
# We will use four methods only(All have time complexity of O(1)):
    #deq.append(element): appends at the right-end of the deque
    #deq.appendleft(element): appends at the left-end of the deque
    #deq.pop(): removes the right-most element and return the element
    #deq.popleft(): removes the left-most element and return the element


#Queue:
import collections

#Initialize
queue = collections.deque()

#Inserting elements at the end of the queue
queue.append(1)
queue.append(2)
queue.append(3)

#print queue
print(queue)

#top of the queue
top = queue.popleft()
queue.appendleft(top)
print(top)
print(queue)

#Clearing queue:
while len(queue) > 0:
    queue.popleft()
print(queue)

print("----------------------------------------------------------------------------")

#Stack

#Initialzie
stack = collections.deque()

#Inserting elements at the end of the stack
stack.append(1)
stack.append(2)
stack.append(3)

#print stack
print(stack)

#LAST OF THE STACK
last = stack.pop()
stack.append(last)
print(last)
print(stack)

#clearing stack
while len(stack) > 0:
    stack.pop()
print(stack)
