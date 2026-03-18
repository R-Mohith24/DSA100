'''You are given the root of a binary search tree and an array queries of size n consisting of positive integers.

Find a 2D array answer of size n where answer[i] = [mini, maxi]:

mini is the largest value in the tree that is smaller than or equal to queries[i].
 If a such value does not exist, add -1 instead.
maxi is the smallest value in the tree that is greater than or equal to queries[i].
 If a such value does not exist, add -1 instead.
Return the array answer.'''





class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def floor(node,k):
            if node is None:
                return -1
            if node.val == k:
                return node.val
            if node.val > k:
                return  floor(node.left , k)

            if node.val < k:
                flr = node.val
                right = floor(node.right , k)
                if right is not -1:
                    return right
                else:
                    return flr

        def ceil(node,k):
            if node is None:
                return -1
            if node.val == k:
                return node.val
            if node.val < k:
                return  ceil(node.right , k)

            if node.val > k:
                cl = node.val
                left = ceil(node.left , k)
                if left is not -1:
                    return left
                else:
                    return cl
        res = []
        for k in queries:
            flr = floor(root,k)
            cl = ceil(root,k)
            res.append([flr,cl])
        return res
