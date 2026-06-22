from collections import deque

def bfs(adj, start):
    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)
    while q:
        x = q.popleft()
        print(x)
        for neighbour in adj[x]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)


adj = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4, 2]
}
print(bfs(adj , 1))


from collections import deque

def bfs(adj, source):
    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)
    while q:
        x = q.popleft()
        if x is destination:
            return True
        for neighbour in adj[x]:
            if neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)
    return False