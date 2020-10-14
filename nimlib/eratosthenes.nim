import math
proc eratosthenes(N:int):bool =
    result = true
    for i in 2..sqrt(N.toFloat).int:
        if N mod i == 0:
            result = false

echo eratosthenes(10000)
echo eratosthenes(10^9 + 7)