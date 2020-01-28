# coding: utf-8

def dijkstra(s, cost, used, V):
    d = [float("inf") for _ in range(V)]
    used = [False for _ in range(V)]
    d[s] = 0
    while True:
        v = -1
        for u in range(V):
            if not used[u] and (v == -1 or d[u] < d[v]):
                v = u
        if v == -1:
            break
        used[v] = True
        for u in range(V):
            d[u] = min(d[u], d[v] + cost[v][u])
    return d

