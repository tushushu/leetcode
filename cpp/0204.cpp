#include <vector>
#include <iostream>
#include <math.h>
using namespace std;

class Solution
{
public:
    inline int helper(int x){
        return x * x;
    }
    int countPrimes(int n)
    {
        if (n < 2){
            return 0;
        }
        vector<int> primes(n, 1);
        primes[0] = 0;
        primes[1] = 0;
        int m = sqrt(n) + 1;
        int ret = 0;
        for (int i = 0; i < m; ++i){
            if (!primes[i]){
                continue;
            }
            for(int j = helper(i); j < n; j += i){
                primes[j] = 0;
            }
        }
        for (int i = 0; i < n; ++i){
            ret += primes[i];
        }
        return ret;
    }
};