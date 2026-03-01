from LLModule import LL , Node

def OddEven(head):
    dummy_odd = Node(0)
    dummy_even = Node(0)

    prev_dummy_odd = dummy_odd
    prev_dummy_even = dummy_even

    while(head is not None):
        next_node = head.next
        head.next = None

        if head.val % 2 != 0:
            prev_dummy_odd.next = head
            prev_dummy_odd = prev_dummy_odd.next
            head = next_node
        else:
            prev_dummy_even.next = head
            prev_dummy_even = prev_dummy_even.next
            head = next_node
    prev_dummy_odd.next = dummy_even.next

    if dummy_odd.next is None:
        return dummy_even.next
    return dummy_odd.next
