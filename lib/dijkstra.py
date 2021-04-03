from heapq import heappop, heappush
def dijkstra(s, N, adj):
    dist = [float("inf")] * N
    visited = [False] * N
    dist[s] = 0
    queue = [(0, s)]
    while queue:
        _, v = heappop(queue)
        visited[v] = True
        for to, cost in adj[v]:
            if cost + dist[v] < dist[to] and not visited[to]:
                dist[to] = dist[v] + cost
                heappush(queue, (dist[to], to))
    return dist

"""AOJ sample
from heapq import heappop, heappush
V, E, r = map(int, input().split())
adj = [[] for _ in range(V)]
# print(adj)
for i in range(E):
    s, t, d = map(int, input().split())
    # print(s, t, d)
    adj[s].append((t, d))

def dijkstra(s, N, adj):
    dist = [float("inf")] * N
    visited = [False] * N
    dist[s] = 0
    queue = [(0, s)]
    while queue:
        _, v = heappop(queue)
        visited[v] = True
        for to, cost in adj[v]:
            if cost + dist[v] < dist[to] and not visited[to]:
                dist[to] = dist[v] + cost
                heappush(queue, (dist[to], to))
    return dist

dist = dijkstra(r, V, adj)
for i in range(V):
    if dist[i] == float("inf"):
        print("INF")
    else:
        print(dist[i])

"""
