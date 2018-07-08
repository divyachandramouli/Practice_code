#Implentation of Queue using lists/arrays and a max size
#Not a linked list type implementation

class Queue:
	def __init__(self,capacity):
		self.front=self.size=0 
		self.rear=capacity-1
		self.capacity=capacity
		self.Q=[None]*capacity
#Front and rear denote the indices 
#Q is initialized to a list of size capacity with none as value

	def isFull(self)
		return self.size==self.capacity

	def enQ(self)