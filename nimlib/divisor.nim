import sequtils, strutils, algorithm, math, future, sets, tables, hashes

proc divisor(N:int):seq =
    result = @[]
    for i in 1..sqrt(N).int + 1:
        if N mod i == 0:
            result.add i
            result.add N div i
