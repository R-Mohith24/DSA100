from LLModule import LL,Node


def findmid(head):
    slow = head
    fast = head.next #since we need to return "first" Middle element for even no of elements for merge sort
    if head is None:
        return head
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow


def MergeLL(h1,h2):
    dummy = Node(0)
    prev = dummy

    while h1 is not None and h2 is not None:
        if h1.val < h2.val:
            prev.next = h1
            h1 = h1.next
        else:
            prev.next = h2
            h2 = h2.next
        prev = prev.next

    if h1 is not None:
        prev.next = h1
    else:
        prev.next = h2
    
    return dummy.next

def SortLL(head):
    if head is None or head.next is None:
        return head
    mid = findmid(head)
    temp = mid.next
    mid.next = None
    
    return MergeLL(SortLL(head) , SortLL(temp))