from LLModule import LL , Node

def size(head):
    count = 0
    while(head is not None):
        count += 1
        head = head.next
    return count

def findIntersection(head1 , head2):
    h1_size = size(head1)
    h2_size = size(head2)

    skip = abs(h1_size - h2_size)

    for _ in range(skip):
        if h1_size > h2_size:
            head1 = head1.next
        else:
            head2 = head2.next

    while(head1 is not None and head2 is not None):
        if head1 != head2:
            head1 = head1.next
            head2 = head2.next
        else:
            return(head1)
    return None # if there is no intersection at all


