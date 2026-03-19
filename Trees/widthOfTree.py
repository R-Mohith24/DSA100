from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        ans = 0
        q = deque([(root, 0)])  # (node, index)
        
        while q:
            size = len(q)
            min_index = q[0][1]  # normalize to avoid overflow
            
            first = last = 0
            
            for i in range(size):
                node, idx = q.popleft()
                
                # normalize index
                cur_id = idx - min_index
                
                if i == 0:
                    first = cur_id
                if i == size - 1:
                    last = cur_id
                
                if node.left:
                    q.append((node.left, cur_id * 2 + 1))
                
                if node.right:
                    q.append((node.right, cur_id * 2 + 2))
            
            ans = max(ans, last - first + 1)
        
        return ans