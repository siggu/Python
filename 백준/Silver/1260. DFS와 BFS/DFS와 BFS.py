from collections import *

def dfs(V):
    visited[V] = True
    print(V, end=" ")

    for i in graph[V]:
        if not visited[i]:
            dfs(i)

def bfs(V):
    queue = deque([V])
    visited[V] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (N+1)
dfs(V)
print()

visited = [False] * (N+1)
bfs(V)