# Implementing Queue using LinkedList and a maxsize

class Element(object):
	def __init__(self,value=None):
		self.value=value
		self.next=None

class Queue(object):
	def __init__(self,head=None):
		self.head=head
		self.size=0
		self.maxsize=4

	def enqueue(self,new_element):
		current=self.head
		
		if(self.head):
			self.size=1
			while(current.next and self.size<=self.maxsize):
				current=current.next
				self.size+=1
			if (self.size>self.maxsize):
				print("Queue is full!")
				return False
			current.next=new_element
		else:
			self.head=new_element
			self.size+=1

	def dequeue(self):
		deleted=self.head
		if(self.head):
			self.head=self.head.next
			deleted.next=None
			self.size=self.size-1
		return deleted

e1=Element(1)
e2=Element(2)
e3=Element(3)
e4=Element(4)
e5=Element(5)

q=Queue()
q.enqueue(e1)
q.enqueue(e2)
q.enqueue(e3)
print(q.head.value)
print(q.head.next.value)
print(q.head.next.next.value)
q.enqueue(e4)
print(q.head.next.next.next.value)
q.enqueue(e5)
print("Dequeued:",q.dequeue().value)
print(q.head.value)
q.enqueue(e5)

print(q.head.next.next.next.value)
