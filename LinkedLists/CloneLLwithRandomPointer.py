"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        def InsertCopies(head):
            temp = head
            while temp:tt
                copynode = Node(temp.val)
                copynode.next = temp.next
                temp.next = copynode
                temp = temp.next.next

        def connectRandomPointers(head):
            temp = head
            while temp:
                copynode = temp.next
                if temp.random == None:
                    copynode.random = None
                    temp = temp.next.next
                else:
                    copynode.random = temp.random.next
                    temp = temp.next.next
        def NextPointer(head):
            dummy = Node(0)
            prev = dummy 

            temp = head
            while temp:
                prev.next = temp.next
                temp.next = temp.next.next
                prev = prev.next
                temp = temp.next
            return dummy.next

        InsertCopies(head)
        connectRandomPointers(head)
        return NextPointer(head)

        