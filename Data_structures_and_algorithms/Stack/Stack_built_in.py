
stack=[]
def view_stack(stack):
		for item in stack:
			print(item)
def push(stack, element):
	stack.append(element)

def pop_out(stack):
	if(stack):
		item=stack.pop()
		return item
	else:
		print("Stack is empty")

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
		view_stack(stack)
	elif (choice==2):
		element=input("Enter the element you want to push on to the stack:")
		push(stack,element)
	elif (choice==3):
		print("Item popped out:",pop_out(stack))
	else:
		return