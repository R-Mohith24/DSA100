from LLModule import LL , Node

def cycleDetection(head:Node):
    slow = head
    fast = head

    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
            break
    return False
