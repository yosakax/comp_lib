import sequtils, strutils, algorithm, math, future, sets, tables, hashes

type UnionFind = object
    n:int
    parents:seq[int]

func initUF(n = 1):UnionFind =
    result.n = n
    result.parents = newSeqWith(n, -1)


proc find(self:initUF, x:int):int =
    # result.parents
    if result.parents[x] < 0:
        return x
    else:
        result.parents[x] = find(result.parents[x])
        return result.parents[x]



