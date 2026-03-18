class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def func(root , curr):
            if root is None:
                return 0
            curr = curr * (10**len(str(root.val))) + root.val
            if root.left is None and root.right is None:
                return curr
            return func(root.left , curr) + func(root.right,curr)
        
        return func(root,0)