from LLModule import LL,Node

def findmid(head):
    slow = head
    fast = head
    if head is None:
        return head
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow