# We will implement st ad queue data structure using Collections.deque()
# We will use four methods only(All have time complexity of O(1)):
# deq.append(element): appends at the ending of the deque(right-end)
# deq.appendleft(element): appends at the begining of the deque(left-end)
# deq.pop(): removes the last/right-most element and return the element
# deq.popleft(): removes the first/left-most element and return the element


#Queue:
import collections

#Initialize
queue = collections.deque()

#Inserting elements at the end of the queue
queue.append(1)
queue.append(2)
queue.append(3)

#Print queue
print(queue)

#First(oldest) element of the queue
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

#Print stack
print(stack)

#Last(newest) element of the stack
last = stack.pop()
stack.append(last)
print(last)
print(stack)

#Clearing stack
while len(stack) > 0:
    stack.pop()
print(stack)
