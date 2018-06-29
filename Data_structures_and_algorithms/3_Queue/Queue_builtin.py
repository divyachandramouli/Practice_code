# Queue using Python's built in functions
# Append adds an element to the tail (newest element) :Enqueue
# Popleft removes and returns the head (oldest element) : Dequeue

from collections import deque
queue=deque(["muffin","cake","pastry"])
print(queue.popleft())
# No operation called popright - you dequeue the head which is the oldest element
queue.append("cookie")
print(queue)

