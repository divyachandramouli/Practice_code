class Element(object):
	def __init__(self,value=None):
		self.value=value
		self.next=None

class Queue(object):
	def __init__(self,node=None):
		self.head=node
		self.tail=node
	
	def enQ(self,new_element):
		if (self.tail):
			"Tail already points to something"
			self.tail.next=new_element
			"Move tail to point to the latest element"
			self.tail=new_element
		else:
			"If it is the first element make head and tail point to that"
			self.head=new_element
			self.tail=new_element

	def deQ(self):
		dequeued=self.head
		if(self.head):
			self.head=self.head.next
			dequeued.next=None
			
		return dequeued
			

q=Queue()
e1=Element(1)
e2=Element(2)
e3=Element(3)
e4=Element(4)
e5=Element(5)
q.enQ(e1)
q.enQ(e2)
q.enQ(e3)
q2=Queue(e1)
q2.enQ(e2)
q2.enQ(e3)
q2.enQ(e4)

print("First element:",q2.head.value)#Prints first element
print("Last element:",q2.tail.value)# Prints last element
print("Dequeued:",q2.deQ().value)
print("First element now:",q2.head.value)
print("Last element:",q2.tail.value)
q2.enQ(e5)
print("Last element:",q2.tail.value)