#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int majorityElement(vector<int> &nums)
    {
        int ret = nums[0];
        int cnt = 0;
        int n = nums.size();
        for (int i = 0; i < n; ++i)
        {
            if (cnt != 0)
            {
                cnt += nums[i] == ret ? 1 : -1;
            }
            else
            {
                ++cnt;
                ret = nums[i];
            }
        }
        return ret;
    }
};