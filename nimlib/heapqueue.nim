import sequtils, strutils, algorithm, math, future, sets, tables, hashes

proc heappush[T](arr:var seq[T], elem:T)=
  var n = arr.len
  arr.add(elem)
  while n != 0:
    var i = (n - 1) div 2
    if arr[n] > arr[i]:
      swap(arr[n],arr[i])
    n = i

proc heappop[T](arr:var seq[T]):T=
  result = arr[0]
 
  var n = arr.len - 1
  arr[0] = arr[n]
  arr.delete(n)
  var i = 0
  var j :int = 2 * i + 1
  while j < n:
    if j != n-1 and arr[j] < arr[j+1]:
      j += 1
    if arr[i] < arr[j]:
      swap(arr[i], arr[j])
    i=j
    j = 2 * i + 1