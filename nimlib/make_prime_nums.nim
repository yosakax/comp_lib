import math, sequtils

proc eratosthenes(N:int):bool =
    result = true
    for i in 2..sqrt(N.toFloat).int:
        if N mod i == 0:
            result = false

proc make_prime_nums(N:int):seq =
    var
        prime_tf = newSeqWith(N+1, true)
        primes = newSeq[int]()
    prime_tf[0] = false
    prime_tf[1] = false
    for i in 0..N:
        if prime_tf[i]:
            if eratosthenes(i):
                for j in countup(i*2, N, i):
                    prime_tf[j] = false
    for i in 0..N:
        if prime_tf[i]:
            primes.add i
    return primes