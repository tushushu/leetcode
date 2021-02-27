#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    inline void helper(int &x, long &y)
    {
        y = y * 10 + x % 10;
        x /= 10;
    }

    bool isPalindrome(int x)
    {
        if (x <= 0)
        {
            return x == 0;
        }
        long y = 0;
        int z = x;
        while (x)
        {
            helper(x, y);
        }

        return z == y;
    }
};