# Linked List Basics


''' 
* Class Element creates a node/ element - single unit of the linked list when provided with the data
* Every object of the class has a 'value' and 'next' variable. __init__ initializes a new element
* 'next' (which points to the next element)is set to None by default for every element - it is modified in the append/insert function 

'''
class Element(object):
	def __init__(self,value):
		self.value=value
		self.next=None


'''
* Class LinkedList takes an object of the element class as argument
* In the constructor, the head element is assigned to the 'element' object which means
  it points to that object  ( holds the memory address of the element object)
* A linkedlist is something that has a 'head element' , 
* If we don't pass the object to which the head should point to, it defaults to none
'''


'''
Add a new element to the end of a list
If the linked list class object is given an element as input, then head points to that element, otherwise head is None
while appending, if the head is pointing to nothing, it will be assigned to point to the element being appended
'''
class LinkedList(object):
	def __init__(self,head=None):
		self.head = head

	def append(self, new_element):
		current = self.head
		if self.head:
			while (current.next):
				current = current.next
			current.next=new_element
		else: 
			self.head=new_element

#Display the elements of a linked list
	
	def display(self):
		elements_list=[]
		current=self.head
		if self.head:
			while(current):
				elements_list.append(current.value)
				current=current.next
			return elements_list
		else:
			return "Linked list is empty!"
#Insert an element into a linked list given the value and position

	def insert(self, ins_element, pos):
		current=self.head
		cur_pos=1

		
		
		if self.head:
			while(current or cur_pos==pos):
				if (cur_pos!=pos):
					current=current.next
					cur_pos+=1
				else:
					if(current==None):

					temp=current.next
					current.next=ins_element
					ins_element.next=temp
					return
		else:
			if(cur_pos==pos):
				self.head=ins_element
				return

		print("Invalid position - out of range")


		

		




	
e1=Element(500)
e2=Element(600)
e3=Element(700)
e4=Element(800)
e5=Element(900)
e6=Element(1000)
l=LinkedList()
l.append(e2)
#l.append(e3)
#print(l.display())
l.insert(e4,2)
print(l.display())
#print(l.display())
#l.insert(e3,2)
#print(l.display())

