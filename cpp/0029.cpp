#include <iostream>
#include <unordered_map>
using namespace std;

unordered_map<int, int> mapping = {
    {-1, INT_MAX},
    {1, INT_MIN},
    {2, -1073741824},
    {-2, 1073741824},
    {INT_MIN, 1},
};

class Solution
{
public:
    int divide(int dividend, int divisor)
    {
        if (dividend == INT_MIN)
        {
            if (mapping.count(divisor))
            {
                return mapping[divisor];
            }
            else
            {
                ++dividend;
            }
        }
        if (divisor == INT_MIN)
        {
            return 0;
        }
        int pos = (dividend > 0) == (divisor > 0);
        int ret = 0;
        dividend = abs(dividend);
        divisor = abs(divisor);
        while (dividend >= divisor)
        {
            long a = 1;
            long b = divisor;
            while (dividend >= b)
            {
                dividend -= b;
                ret += a;
                a = a << 1;
                b = b << 1;
            }
        }
        return pos ? ret : -ret;
    }
};