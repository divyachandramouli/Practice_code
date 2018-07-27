
class stack_class():

	def __init__(self):
		self.a_stack=[]

	def view_stack(self):
		if(self.a_stack):
			for item in self.a_stack:
				print(item)
		else:
			print("Stack is empty!")
			
	def push(self, element):
		self.a_stack.append(element)

	def pop_out(self):
		if(self.a_stack):
			item=self.a_stack.pop()
			return item
		else:
			print("Stack is empty")


stack=stack_class()

while True:
	print("*********************************")
	print("Stack using Built In Functions")
	print("*********************************")
	print("1: View Stack")
	print("2: Push an element")
	print("3: Pop an element")
	print("______________________________")
	choice=int(input("Enter the choice number:"))

	if (choice==1):
		stack.view_stack()
	elif (choice==2):
		element=input("Enter the element you want to push on to the stack:")
		stack.push(element)
	elif (choice==3):
		print("Item popped out:",stack.pop_out())
	else:
		break