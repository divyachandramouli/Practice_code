class Queue(object):

	def __init__(self,head=None):
		self.storage=[head]

	def enqueue(self, new_element):
		self.storage.append(new_element) # appends to the tail (newest element)

	def peek(self):
		return self.storage[0] # Look at the head

	def dequeue(self):
		return self.storage.pop(0) # Pop acts on the oldest element 


q=Queue(1)
q.enqueue(2)
q.enqueue(3)


print (q.peek())
print (q.dequeue())

q.enqueue(4)
print (q.dequeue())
print (q.dequeue())
print(q.peek())