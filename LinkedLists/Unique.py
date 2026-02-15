'''Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.
 Return the linked list sorted as well.'''

'''
Input: head = [1,1,1,2,3]
Output: [2,3]
'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Create dummy node
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while head is not None:

            # Check if duplicate block exists
            if head.next is not None and head.val == head.next.val:

                # Skip all nodes with same value
                while head.next is not None and head.val == head.next.val:
                    head = head.next

                # Remove entire duplicate block
                prev.next = head.next

            else:
                # Current node is unique
                prev = prev.next

            # Move head forward
            head = head.next

        return dummy.next
