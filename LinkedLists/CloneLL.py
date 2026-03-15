from LLModule import LL , Node

class Solution:
    def cloneLL(self, head: 'Node') -> 'Node':
        dummy = Node(0)
        temp = dummy
        while(head):
            temp.next = Node(head.val)
            temp = temp.next
            head = head.next
        return dummy.next