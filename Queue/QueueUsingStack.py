stack1 = [] #main stack
stack2 = [] #Helper stack

def enqueue(x):
    while stack1:
        stack2.append(stack1.pop())
        
    stack1.append(x)
    while stack2:
        stack1.append(stack2.pop())
        
def dequeue():
    if not stack1: #if stack 1 is empty
        print("The queue is Empty")
        return None
    return stack1.pop()

def IsEmpty():
    return len() == 0 

def peek():
    if not stack1:
        return None
    return stack1[-1]


def size():
    return len(stack1)

