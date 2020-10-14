import sequtils, strutils, algorithm, math, future, sets, tables, hashes
proc `ceilDiv`*[T](x, y: T): T = x div y + ord(x mod y != 0)
proc `//=`*(x: var SomeInteger; y: SomeInteger) = x = x div y
proc `%=`*(x: var SomeInteger; y: SomeInteger) = x = x mod y

proc cmb(n, k, M:int, fac, ifac:seq[int]):int =
    var k = min(k, n-k)
    return fac[n] * ifac[k] * ifac[n-k] mod M

proc make_tables(M, n:int):seq[seq[int]] = 
    var
        fac = @[1, 1]   # 階乗テーブル
        ifac = @[1, 1]  # 逆元の階乗テーブル
        inverse = @[0, 1]  # 逆元テーブル
    for i in 2..n:
        fac.add (fac[^1] * i) mod M
        inverse.add (-inverse[M mod i] * (M div i)) mod M
        ifac.add (ifac[^1] * inverse[^1]) mod M
    return @[fac, ifac]
