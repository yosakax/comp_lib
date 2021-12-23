#include <bits/stdc++.h>
using namespace std;
#define rep(i, s, e) for (int i = s; i < e; ++i)
template <typename T>
map<T, int> make_primes(long N)
{
    map<long, int> primes;
    rep(i, 0, sqrt((double)N) + 1)
    {
        if (N % i == 0)
        {
            primes[i] = 0;
            while (N % i == 0)
            {
                primes[i]++;
                N /= i;
            }
        }
    }
    if (N > 1)
    {
        primes[N] = 1;
    }
    return primes;
}