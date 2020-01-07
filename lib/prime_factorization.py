#coding: utf-8

def prime_factorization(N):
    # 辞書型で素因数分解を返す
    pf = {}
    for i in range(2, int(N**0.5) + 1):
        while N % i == 0:
            if i not in pf.keys():
                pf[i] = 1
            else:
                pf[i] += 1
            N //= i
    if N > 1:
        pf[N] = 1
    return pf