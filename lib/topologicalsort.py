from collections import defaultdict, deque


def topological_sort(G, into_num, V):
    # 入ってくる有向辺を持たないノードを列挙
    q = deque()
    # V: 頂点数
    for i in range(V):
        if into_num[i] == 0:
            q.append(i)

    # 以下、幅優先探索
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1  # 入次数を減らす
            if into_num[adj] == 0:
                q.append(adj)  # 入次数が0になったら、キューに入れる

    return ans
