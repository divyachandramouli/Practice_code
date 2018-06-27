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

class Stack(object):
    def __init__(self,top=None):
        self.ll=Linkedlist(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        self.ll.delete_first(new_element)


e1=Element(1)
e2=Element(2)
e3=Element(3)

stack=Stack(e1)
stack.push(e2)
stack.push(e3)

print (stack.pop().value)