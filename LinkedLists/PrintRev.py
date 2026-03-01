from LLModule import Node,LL


def printRev(n):
    if (n == None):
        return

    printRev(n.next)
    print(n.val)

