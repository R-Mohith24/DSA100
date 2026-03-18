class Solution:

    def hasPathSum(self, root, target):
        '''
        :param root: root of given tree.
        :param sm: root to leaf sum
        :return: true or false
        '''
        if root is None: return False
        target -= root.data
        if target == 0 and root.left is None and root.right is None:
            return True
        return self.hasPathSum(root.left,target) or self.hasPathSum(root.right,target)

'''Given a binary tree and an integer target,
check whether there is a root-to-leaf path with its sum as target.'''