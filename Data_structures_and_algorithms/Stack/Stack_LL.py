# Implement a stack using a linked list

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert_first(self,new_element):
    	new_element.next=self.head
    	self.head=new_element

    def delete_first(self):
    	
    	deleted=self.head
    	if self.head:
    		self.head=self.head.next
    		deleted.next=None
    	return deleted 
    	


	
e1=Element(1)
e2=Element(2)
e3=Element(3)

ll=LinkedList()
#ll.insert_first(e1)
#print(ll.head)
ll.insert_first(e1)
ll.insert_first(e2)
ll.insert_first(e3)
print(ll.head.next.next.value)