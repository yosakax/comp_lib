def Base_10_to_n(X, n):
    if int(X / n):
        return Base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)


def Base_n_to_10(X, n):
    out = 0
    for i in range(1, len(str(X)) + 1):
        out += int(X[-i]) * (n ** (i - 1))
    return out  # int out
