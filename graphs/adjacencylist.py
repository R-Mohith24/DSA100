from collections import defaultdict

n, m = map(int, input().split())

adj = defaultdict(list)
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u,v))
for u , v in edges:
    adj[u].append(v)


