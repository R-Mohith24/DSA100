def maxPath(root : Optional[TreeNode] , maxi:int) -> int:
    if root is None:
        return 0
    leftsum = max(0,maxPath(root.left , maxi))
    rightsum = max(0,maxPath(root.right , maxi))
    maxi = max(maxi , leftsum + rightsum + root.val)
    return root.val + max(leftsum , rightsum)