from LLModule import LL,Node

def MergeSortedLL(h1 , h2):
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
