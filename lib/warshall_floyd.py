for k in range(V):
    for i in range(V):
        for j in range(V):
            if cost[i][k]!=INF and cost[k][j]!=INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])