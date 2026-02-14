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
            self.tail = new_node
            return
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
    