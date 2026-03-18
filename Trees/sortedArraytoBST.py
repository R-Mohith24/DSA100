def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid+1:])
    
    return root


'''example:
nums = [1, 2, 3, 4, 5]
        0  1  2  3  4

nums[:mid] means nums[0] to nums[mid-1]
nums[:2] = [1, 2]  ← everything BEFORE mid

nums[mid+1:] means nums[mid+1] to end
nums[3:] = [4, 5]  ← everything AFTER mid

        3          ← nums[2] (mid)
       / \
  [1,2]   [4,5]    ← left half | right half
'''

