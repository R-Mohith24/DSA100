'''
given an function that accepts int N func(int N){ }
ex : if N = 5 then , create a linked list from 1 to 5 (1-->2-->3-->4-->5-->null)
and return the head
'''
@abstract 
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
class LL:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertnode(self,val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

# for SLL
def create_list(N):
    if N <= 0:
        return None

    head = Node(1)        # Create first node
    temp = head           # Keep reference to head

    for i in range(2, N + 1):
        temp.next = Node(i)   # Attach new node
        temp = temp.next      # Move forward

    return head

# For Circularly SLL

def create_list(N):
    if N <= 0:
        return None

    head = Node(1)        # Create first node
    temp = head           # Keep reference to head

    for i in range(2, N + 1):
        temp.next = Node(i)   # Attach new node
        temp = temp.next      # Move forward
    temp.next = head # KEY POINT FOR CSLL
    return head


# for DLL

def create_list(N):
    if N <= 0:
        return None

    head = Node(1)        # Create first node
    temp = head           # Keep reference to head

    for i in range(2, N + 1):
        temp.next = Node(i)  #attach new node
        temp.next.prev = temp  # connect prev pointer to temp
        temp = temp.next      # Move forward

    return head


#for CDLL

def create_list(N):
    if N <= 0:
        return None

    head = Node(1)        # Create first node
    temp = head           # Keep reference to head

    for i in range(2, N + 1):
        temp.next = Node(i)  #attach new node
        temp.next.prev = temp  # connect prev pointer to temp
        temp = temp.next      # Move forward
    temp.next = head
    head.prev = temp
    return head