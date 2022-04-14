from collections import defaultdict

# example:https://atcoder.jp/contests/abc177/tasks/abc177_e
class FastPrimeFactorizer:
    """高速素因数分解"""

    def __init__(self, n=10**7) -> None:
        """D[i] = iの最小の素因数となる配列を作成

        Parameters
        ----------
        n : int, 上限
            返せる値の上限O(N), by default 10**7
        """
        self.n = n
        self.D = self.make_primes()

    def make_primes(self):
        """Dを作る"""
        D = [i for i in range(self.n + 1)]
        for i in range(2, self.n + 1):
            if D[i] == i:
                for j in range(i, self.n + 1, i):
                    D[j] = i
        return D

    def factorize(self, v):
        """Dを用いてvの素因数分解を行う"""
        primes = defaultdict(int)
        while v > 1:
            p = self.D[v]
            while v % p == 0:
                v //= p
                primes[p] += 1
        return primes
