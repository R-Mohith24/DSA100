#GRAPH

```py
def dfs(graph, node, visited):
    if node in visited:
        return
    
    visited.add(node)
    print(node)  # or do whatever you need with this node
    
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)
```


#### here graph[node] ==> adacency list
```
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

ante A has B and C as neighbors ani


# BFS

```py
from collections import deque

def bfs(adj, source):
    visited = set()
    q = deque()
    q.append(source)
    visited.add(source)
    result = []

    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in adj[node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

    return result
```