from collections import deque
q1 = deque()
q2 = deque()

def push(x):
    q2.append(x)
    while q1:
        q2.append(q1.popleft())
    q1 , q2 = q2 , q1
    
def pop():
    if not q1: #q1 is empty
        print("the stack is empty")
        return None
    return q1.popleft()

def peek():
    if not q1:
        return None
    return q1[0]

def size():
    return len(q1)
def IsEmpty():
    return len(q1) == 0

