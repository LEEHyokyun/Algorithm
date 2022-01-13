stack = [1,2,3,4]

stack.append(7)
print(stack)
stack.pop()
print(stack)

print(stack)

##queue = [1,2,3,4]

from queue import Queue
queue = Queue()

queue.put(2)
print(queue.queue)
queue.put(3)
print(queue.queue)
queue.put(4)
print(queue.queue)
queue.get()
print(queue.queue)