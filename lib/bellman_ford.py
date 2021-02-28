INF = float("inf")
def bellman_ford(s, N, g):
    dist = [INF] * N
    dist[s] = 0
    for i in range(N):
        update = False
        for fro, to, cost in g:
            if dist[to] > dist[fro] + cost:
                dist[to] = dist[fro] + cost
                update = True
        if not update:
            return dist
        # 負の経路が存在
        if i == N - 1:
            return -1

if __name__ == "__main__":
    ## https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_B
    V, E, r = map(int, input().split())
    adj = []
    # print(adj)
    for i in range(E):
        s, t, d = map(int, input().split())
        # print(s, t, d)
        adj.append((s, t, d))
    dist = bellman_ford(r, V, adj)
    if dist == -1:
        print("NEGATIVE CYCLE")
    else:
        print(*[d if d != INF else "INF" for d in dist], sep="\n")