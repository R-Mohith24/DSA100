def func(root  , col):
    if root == None:
        return 

    if col not in hashmap:
        hashmap[col] = []
    hashmap[col].append(root.val)

    func(root.left ,  col+1)
    func(root.right ,  col)
hashmap = {}
func(root , 0)
for col in sorted(hashmap): 
    print(hashmap[col])