from LLModule import Node,LL

def DelAtPos(head , pos):
    if(pos<0 or pos>=size(head)):
        return head
    if(pos == 0):
        return head.next
    temp = head
    for i in range(pos-1):
        temp = temp.next

    temp.next = temp.next.next
    return head


def size(head):
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    return count

# 1 --> 2 --> 3 --> 4 --> 5
# 0     1     2     3     4
