class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def InsertAtTail(self,value):
        new_node = node(value)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node

    def PrintList(self):
        temp = self.head
        while temp != None:
            print(temp.value, end="->")
            temp = temp.next
    def InsertAtHead(self,value):
        new_node = node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node


    def InsertAtK(self,value,K):
        if K == 0:
            self.InsertAtHead(value)
            return

        temp = self.head
        count = 0
        while temp is not None and count < K-1:
            temp = temp.next
            count += 1
        if temp is None:
            print("out of range")
            return

        new_node = node(value)
        new_node.next = temp.next
        temp.next = new_node
        
        if new_node.next is None:
            self.tail = new_node
    
    def DeleteAtHead(self):

        if self.head is None:
            print("List is empty")
            return

        # If only one node
        if self.head.next is None:
            self.head = None
            self.tail = None
            return

        # Move head forward
        self.head = self.head.next

    def DeleteAtTail(self):

        if self.head is None:
            print("List is empty")
            return

        # If only one node
        if self.head.next is None:
            self.head = None
            self.tail = None
            return

        temp = self.head

        # Move to second-last node
        while temp.next != self.tail:
            temp = temp.next

        temp.next = None
        self.tail = temp

    def DeleteAtK(self, K):

        if self.head is None:
            print("List is empty")
            return

        # Delete head
        if K == 0:
            self.DeleteAtHead()
            return

        temp = self.head
        count = 0

        # Move to node at index K-1
        while temp.next is not None and count < K - 1:
            temp = temp.next
            count += 1

        # If K out of range
        if temp.next is None:
            print("Index out of range")
            return

        # If deleting tail
        if temp.next == self.tail:
            self.tail = temp

        # Skip the node
        temp.next = temp.next.next
