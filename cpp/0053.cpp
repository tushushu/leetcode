#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int ret = INT_MIN;
        int cur = 0;
        vector<int>::iterator end = nums.end();
        for (vector<int>::iterator it = nums.begin(); it != end; ++it)
        {
            cur += *it;
            if (cur > ret)
                ret = cur;
            if (cur < 0)
                cur = 0;
        }
        return ret;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    // vector<int> v = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    vector<int> v = {-2};
    cout << s.maxSubArray(v) << endl;
    return 0;
}
