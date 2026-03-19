def path(root : Optional[TreeNode] , x : Optional[TreeNode] , ls : List[int]) -> bool:
    if root == None:
        return False
    if root.val == x or path(root.left , x , ls) == True or path(root.right , x , ls) == True :
        ls.append(root)
        return True
    return False

def findPathLenght(root : Optional[TreeNode] , x: Optional[TreeNode] , y:Optional[TreeNode]):
    ls1 = []
    ls2 = []
    path(root, x , ls1)
    path(root , y , ls2)
    ls1.reverse()
    ls2.reverse()
    p1 = 0
    p2 = 0
    while p1 < len(ls1) and p2 < len(ls2) and ls1[p1] == ls2[p2] : 
        p1 += 1
        p2 += 1
    return (len(ls1) - p1) + (len(ls2) - p2)