class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None


# state variables (instead of self.*)
capacity = 0
hashmap = {}
LRU = None
MRU = None


def init(cap):
    global capacity, hashmap, LRU, MRU
    capacity = cap
    hashmap = {}

    LRU = Node(0, 0)
    MRU = Node(0, 0)

    LRU.next = MRU
    MRU.prev = LRU


# remove from the list
def remove(node):
    prev = node.prev
    nxt = node.next
    prev.next = nxt
    nxt.prev = prev


# insert at the MRU.next
def insert(node):
    global MRU
    prev = MRU.prev
    nxt = MRU
    prev.next = nxt.prev = node
    node.next, node.prev = nxt, prev


def get(key: int) -> int:
    if key in hashmap:
        remove(hashmap[key])
        insert(hashmap[key])
        return hashmap[key].val
    else:
        return -1


def put(key: int, val: int) -> None:
    if key in hashmap:
        remove(hashmap[key])

    hashmap[key] = Node(key, val)
    insert(hashmap[key])

    if len(hashmap) > capacity:
        least_recently_used = LRU.next
        remove(least_recently_used)
        del hashmap[least_recently_used.key]