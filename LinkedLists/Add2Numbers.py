'''You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
'''Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.'''

from LLModule import LL , Node

def Add2Nums(h1:Node , h2:Node):

    dummy = Node(0)
    prev = dummy

    carry = 0
    Sum = 0
    while h1 or h2 or carry:
        v1 = h1.val if h1 else 0
        v2 = h2.val if h2 else 0

        # Calculate Sum
        Sum = v1 + v2 + carry
        #separate the whole sum into single node and a carry
        carry = Sum // 10
        Sum = Sum % 10
        # create a new node with the new sum
        prev.next = Node(Sum)

        #Move Pointers
        prev = prev.next
        h1 = h1.next if h1 else None
        h2 = h2.next if h2 else None

    return dummy.next

