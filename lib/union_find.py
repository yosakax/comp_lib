#coding: utf-8

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        # xの根を探索
        if self.parents[x] < 0:
            return x
        else:
            # 再帰的に根を探索
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        # 2つの木をマージする。
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def are_same(self, x, y):
        # 2つの要素の根が同じかどうかを調べる
        return self.find(x) == self.find(y)

    def members(self, x):
        # xと同じ根の要素をリストで出力
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == self.n]

    def roots(self):
        # 根である要素をリストで出力
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return "\n".join("{} {}".format(r, self.members(r)) for r in self.roots())
