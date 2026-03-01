'''
delete all node containing X as the Value func(Node h , int x){ } return head
'''

from LLModule import Node,LL

def DelAllX(head , val):
    if head is None:
        return head
    temp = head #i know i should use temp as iterator but i realised it too late and too lazy to change it
    while(head.next is not None):
        if(head.next.val == val):
            head.next = head.next.next
        else:
            head = head.next
    if(temp.val == val):
        return temp.next

    return temp