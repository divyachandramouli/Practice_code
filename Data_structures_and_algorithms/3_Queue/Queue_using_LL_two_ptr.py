class Element(object):
	def __init__(self,value=None):
		self.value=value
		self.next=None

class Queue(object):
	def __init__(self,head=None):
		self.head=None
		self.tail=None
	
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
			self.size=self.size-1
		return dequeued
			

