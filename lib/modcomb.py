def modcomb(n, r, mod):
    """高速な組合せ計算"""
    r = min(r, n - r)
    X, Y = 1, 1
    for i in range(1, r + 1):
        X = X * (n + 1 - i) % mod
        Y = Y * i % mod
    return X * pow(Y, mod - 2, mod) % mod
