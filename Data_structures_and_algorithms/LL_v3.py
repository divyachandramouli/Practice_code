
class Element (object):
	def __init__ (self, value):
		self.value=value
		self.next=None

e1=Element(500)
e2=Element(100)
e3=Element(400)

class LinkedList(object):
	def __init__(self,head=None):
		self.head=head   # 'head' refers to the element you pass while creating a linked list object l=LinkedList(e1)
		 				 #printing l.head gives memory address of e1

	def append(self, new_element):
		current = self.head
		if(current):
			while(current.next):
				current=current.next
			current.next=new_element
		else:
			self.head=new_element

	def display(self):
		current = self.head
		if (current):
			while(current):
				print(current.value)
				current=current.next
		else:
			print(current)
			print('There is only one element')

l=LinkedList(e1)
l.append(e2)
l.append(e3)
l.display()
