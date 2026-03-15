from LLModule import LL , Node

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return fast
        return None

    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        # Find the tail of the list
        tail = head
        while tail.next:
            tail = tail.next

        # Find the cycle
        cycle = self.detectCycle(head)
        if not cycle:
            return head

        # Find the node before the cycle
        prev = head
        while prev.next != cycle:
            prev = prev.next

        # Flatten the list
        tail.next = cycle
        prev.next = None

        return head


