#include <iostream>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int climbStairs(int n)
    {
        if (n < 4)
        {
            return n;
        }
        int a = 2;
        int b = 3;
        for (; n >= 4; --n)
        {
            a += b;
            swap(a, b);
        }
        return b;
    }
};

int main(int argc, char const *argv[])
{
    /* code */
    Solution s;
    cout << 1 << ':' << s.climbStairs(1) << endl;
    cout << 2 << ':' << s.climbStairs(2) << endl;
    cout << 3 << ':' << s.climbStairs(3) << endl;
    cout << 4 << ':' << s.climbStairs(4) << endl;
    cout << 5 << ':' << s.climbStairs(5) << endl;
    cout << 6 << ':' << s.climbStairs(6) << endl;
    return 0;
}
