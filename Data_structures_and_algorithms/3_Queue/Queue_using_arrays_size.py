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
	def isEmpty(self):
		return self.size==0

	def enQ(self):
		"Changes rear and size"
		"You have an array of size n and an index i into that array."
		"Increment i so that it points to the next position in the array,"
		"but have i return to the first position once the end of the"
		" array is reached. - circular increment using % operator"
	
		if(! (self.isFull()):
			self.rear= (self.rear+1)%self.capacity
			self.Q[self.rear]=item
			self.size=self.size+1
		else:
			print("Queue is full!")

	def deQ(self):
		if (!self.isEmpty()):
			dequeued=self.Q[self.front]
			self.front=(self.front+1)%self.capacity
			self.size=self.size-1
			return dequeued
		else:
			print("Queue is empty!")
			return


 # Function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is",  self.Q[self.rear])

    #Function to get front of queue
	def que_front(self):
        if self.isEmpty():
            print("Queue is empty")
 
        print("Front item is", self.Q[self.front])
         
