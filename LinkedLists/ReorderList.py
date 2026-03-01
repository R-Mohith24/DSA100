from LLModule import LL,Node

def FindMid(head):
    slow = head
    fast = head.next
    if head is None:
        return head
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow

def rev(head):
    prev = None 
    while(head != None):
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev

def reorder(h1, h2):

    while h1 is not None and h2 is not None:

        next1 = h1.next
        next2 = h2.next

        h1.next = h2
        h2.next = next1

        h1 = next1
        h2 = next2  

def func(head):

    if head is None or head.next is None:
        return head

    mid = FindMid(head)

    second = mid.next
    mid.next = None

    second = rev(second)

    reorder(head, second)

    return head



    