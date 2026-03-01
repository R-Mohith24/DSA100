#stack basics

#we can implement stack using list
stack = []
#push operation
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after push operations:", stack)

#pop operation
popped_element = stack.pop()
print("Popped element:", popped_element)
print("Stack after pop operation:", stack)

#peek operation
peeked_element = stack[-1]
print("Peeked element:", peeked_element)
print("Stack after peek operation:", stack) 