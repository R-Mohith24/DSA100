from LLModule import Node,LL

def InsertAtSorted(head,val):
    n = Node(val)
    if(head == None or val<head.val):
        n.next = head
        return n
    temp = head
    while(head.next != None and head.next.val < val):
        head = head.next
    n.next = head.next
    head.next = n

    return temp
