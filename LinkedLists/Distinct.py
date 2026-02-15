'''
Given the head of a sorted linked list, the goal is to delete all duplicate elements
 so each number appears only once.
 The sorted property ensures that duplicates appear consecutively, simplifying detection.
 The function should modify the list in place and return the head of the updated list.

Input: 1 → 1 → 2 → 3 → 3
Output: 1 → 2 → 3
'''

from LLModule import Node,LL

def distinct(head):
    if head is None:
        return head
    temp = head
    while(temp.next is not None):
        if(temp.next.val == temp.val):
            temp.next = temp.next.next
        else:
            temp = temp.next
    return head