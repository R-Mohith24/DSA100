from LLModule import Node , LinkedList
class Solution:
    def reverse(self,head):
        prev = None 
        while(head != None):
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

    def findKthNode(self,temp,k):
        k -= 1
        while(temp is not None and k>0):
            k -= 1
            temp = temp.next
        return temp
    
    def reverseKGroup(self, head: Node, k: int) -> Node:
        temp = head
        prevNode = None
        while temp:
            K = self.findKthNode(temp,k)
            if K == None:
                if prevNode:
                    prevNode.next = temp
                break
            nextNode = K.next
            K.next = None
            self.reverse(temp)
            if temp == head:
                head = K
            else:
                prevNode.next = K
            prevNode = temp
            temp = nextNode
        return head
