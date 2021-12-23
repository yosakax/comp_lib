# 逆元のテーブルを作成
def cmb(n, k, mod, fac, ifac):    
    k = min(k, n-k)
    return fac[n] * ifac[k] * ifac[n-k] % mod


def make_tables(mod, n):
    fac = [1, 1]  # 階乗テーブル・・・(1)
    ifac = [1, 1]  # 逆元の階乗テーブル・・・(2)
    inverse = [0, 1]  # 逆元テーブル・・・(3)

    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        ifac.append((ifac[-1] * inverse[-1]) % mod)
    return fac, ifac


"""usage
fac, ifac = make_tables(mod, N)
# nCkを求める
x = cmb(n, k, mod, fac, ifac)
"""