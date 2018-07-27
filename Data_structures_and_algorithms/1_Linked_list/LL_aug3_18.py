# LINKED LIST

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




	def get_length(self):
		current=self.head
		len=0
		while (current):
			len+=1
			current=current.next
		return len

	def append(self, new_element):
		current = self.head
		if(self.head):
			while(current.next):
				current=current.next
			current.next=new_element
		else:
			self.head=new_element

	def display(self):
		current = self.head
		print("Printing linked list ...")
		if (self.head):
			while(current):
				print(current.value)
				current=current.next
		else:
			print('LinkedList is empty!')

	

	def insert(self, ins_element,pos):
		current=self.head
		counter=1
		if(pos>0 and pos<= self.get_length()+1):
			if (pos > 1):
				while(current and counter < pos):
					if counter == pos-1:
						ins_element.next = current.next
						current.next=ins_element
					current=current.next
					counter+=1
			elif (pos == 1):
				ins_element.next=self.head
				self.head=ins_element
		else:
			print("Position out of range to insert!")


	def get_index(self,val):
	 # Returns index/ position of a the value (first occurrence)
		current = self.head
		if(self.head):
			counter=0
			while(current and current.value!=val):
					counter+=1
					current=current.next
			if(current):  
			# While exiting the loop, if it has already reached the end
			#, then none should be returned. Only if the loop stopped because 
			# of value match, it returns an index
				return counter+1
			else:
				return None
		else:
			print("Linked list is empty")


	def get_pos_val(self,pos):
		counter=1
		current=self.head
		if (pos <1 or pos > self.get_length()):
			return None
		while (current and counter <= pos):
			if counter == pos:
				return current.value
				# current will return the address of the element
				#To return the value use current.value
			current=current.next
			counter+=1
		return None


	def delete(self, value):
	        current = self.head
	        previous = None
	        while current.value != value and current.next:
	            previous = current
	            current = current.next
	        if current.value == value:
	            if previous:
	            	# If the value got matched and it's not the 1st element
	            	# prev should have changed 
	                previous.next = current.next
	            else:
	            	#if the first element needs to be deleted
	                self.head = current.next 
	                # current.next which is none for the 1st elem in a 
	                # single element list
	                # Or head points to the second element
	        else: # Value not matched but exit from loop after reaching none for next
	        	print("Element not in the list")

#Detect loop in a linked list
#Given a linked list, check if the the linked list has loop or not. 
	def detect_loop(self):
		current=self.head
		locations=set()
		while(current):
			if current in locations:
				return True
			locations.add(current)
			current=current.next
		return False












e1=Element(500)
e2=Element(100)
e3=Element(400)
e4=Element(3)
e5=Element(10)
		
# Displays empty LL
l=LinkedList()
m=LinkedList()
#l.display()
l.append(e1)
l.append(e2)
l.append(e3)
l.append(e4)
l.append(e5)
l.append(e1)



#print("Position returned:", m.get_index(3))
#print("Value returned:", l.get_pos_val(1))


if(l.detect_loop()):
		print('Loop found')
else:
	print('No loop in list')

