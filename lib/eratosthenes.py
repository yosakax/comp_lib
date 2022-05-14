def eratosthenes(N):
    # 素数判定
    flag = True
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            flag = False
            break
    return flag
