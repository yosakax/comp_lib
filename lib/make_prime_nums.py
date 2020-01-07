#coding: utf-8

def eratosthenes(N):
    # 素数判定
    flag = True
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            flag = False
            break
    return flag

def make_prime_nums(N):
    # Nまでの素数のリストを作成
    prime_tf = [True for _ in range(N+1)]
    prime_tf[0] = False
    prime_tf[1] = False
    for i in range(N+1):
        if prime_tf[i]:
            if eratosthenes(i):
                for j in range(i*2, N+1, i):
                    prime_tf[j] = False
    primes = [i for i in range(N+1) if prime_tf[i]]
    return primes


