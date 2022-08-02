from queue import PriorityQueue

#Initialize
q = PriorityQueue()
q.put((10,'Red balls'))
q.put((8,'Pink balls'))
q.put((5,'White balls'))
q.put((4,'Green balls'))

#Getting the first element(least value) and removing from queue
while not q.empty():
    item = q.get()
    print(item)
