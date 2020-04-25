#coding: utf-8
def divisor(N):
    # 約数列挙
    divs = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            divs.append(i)
            if i != N // i:
                divs.append(N//i)
    return divs