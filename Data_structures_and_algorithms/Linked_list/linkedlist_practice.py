# Linked list - version 1
class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linkedlist(object):
	def __init__(self):
		self.head=node()

	def append(self,data):
		new_node=node(data)
		current=self.head
		while(current.next):
			current=current.next
		current.next=new_node

	def display(self):
		ele=[]
		curr=self.head
		while(curr.next!=None):
			curr=curr.next
			ele.append(curr.data)
		print(ele)
		
	
	def insert(self,data,pos):
		new_data=node(data)
		cur_pos=1
		curr=self.head
		while(curr.next or cur_pos==pos):
				if (cur_pos!=pos):
					curr=curr.next
					cur_pos +=1
				else:
					temp=curr.next
					curr.next=new_data
					new_data.next=temp	
					return

		print("ERROR! Position invalid")
				
			
			
	def delete(self,value):
		curr=self.head
		while(curr.next):
			last_node=curr
			curr=curr.next
			if (curr.data==value):
				last_node.next=curr.next

	def get_pos(self,value):
		curr=self.head
		cur_pos=0
		while(curr.next):
			curr=curr.next
			cur_pos+=1
			if (curr.data==value):
				break
		print(cur_pos)

	def get_length(self):
		len=0;
		current=self.head
		while(current.next):
			current=current.next
			len+=1 
		print(len)
		return len




				

ll=linkedlist()
ll.insert(5,2)
ll.display()