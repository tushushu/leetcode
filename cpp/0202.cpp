#include <iostream>
#include <algorithm>
#include <unordered_set>
using namespace std;

class Solution
{
public:
    inline int helper(int n)
    {
        int m = n % 10;
        return m * m;
    }
    bool isHappy(int n)
    {
        int tot = 0;
        unordered_set<int> record;
        while (!record.count(n))
        {
            record.insert(n);
            while (n != 0)
            {
                tot += helper(n);
                n = n / 10;
            }
            swap(tot, n);
        }
        return n == 1;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    s.isHappy(19);
    return 0;
}
