def func(root , hashmap , col):
    if root == None:
        return 

    if col not in hashmap:
        hashmap[col] = []
    hashmap[col].append(root.val)

    func(root.left , hashmap , col-1)
    func(root.right , hashmap , col + 1)

hashmap = {}
for col in sorted(hashmap):
    print(hashmap[col])