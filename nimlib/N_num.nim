
proc Base_10_to_n(X, n:int): string =
    if X div n != 0:
        return Base_10_to_n(X div n, n) & $(X mod n)
    return $(X mod n)
