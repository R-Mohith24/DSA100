# iterative method 
from LLModule import Node , LL
prev = None 
while(head != None):
    temp = head.next
    head.next = prev
    prev = head
    head = temp

return prev

#recursive method 

def RevR(head):
    if head == None or head.next == None:
        return head
    n = RevR(head.next)
    head.next.next = head
    head.next = None
    return n