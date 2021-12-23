vector<int> topological_sort(vector<vector<int>> &G, vector<int> &indeg, int V)
{
    // トポロジカルソートを記録する配列
    vector<int> sorted_vertives;
    // 入力次数0を見つけたら処理待ちの頂点としてqueueに追加
    queue<int> que;
    rep(i, 0, V)
    {
        if (indeg[i] == 0)
            que.push(i);
    }

    while (que.empty() == false)
    {
        int v = que.front();
        que.pop();

        // 頂点と隣接している頂点の次数を減らし，0になればqueに追加
        rep(i, 0, G[v].size())
        {
            int u = G[v][i];
            indeg[u]--;
            if (indeg[u] == 0)
                que.push(u);
        }
        sorted_vertives.push_back(v);
    }
    return sorted_vertives;
}
