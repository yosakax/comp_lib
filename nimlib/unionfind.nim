import deques, strformat, streams, sequtils, strutils, algorithm, math, future, sets, tables, hashes
proc `ceilDiv`*[T](x, y: T): T = x div y + ord(x mod y != 0)
proc `//`*[T](x, y: T): T = x div y 
proc `%`*[T](x, y: T): T = x mod y 
proc `//=`*(x: var SomeInteger; y: SomeInteger) = x = x div y
proc `%=`*(x: var SomeInteger; y: SomeInteger) = x = x mod y
proc modpow(x: SomeInteger, y:SomeInteger, M:SomeInteger):SomeInteger =
    if x < 0:
        return x + ceilDiv(abs(x), M) * M
    if y <= 0:
        return 1
    elif y % 2 == 0:
        return modpow(x, y//2, M)^2 % M
    else:
        return modpow(x, y-1, M) * x % M

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



