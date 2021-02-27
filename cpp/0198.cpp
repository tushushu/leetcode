#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    inline int helper(vector<int> &nums, int i)
    {
        return max(nums[i - 1], nums[i - 2] + nums[i]);
    }

    int rob(vector<int> &nums)
    {
        int n = nums.size();
        if (n == 0)
        {
            return 0;
        }
        if (n == 1)
        {
            return nums[0];
        }
        nums[1] = max(nums[0], nums[1]);
        for (int i = 2; i < n; ++i)
        {
            nums[i] = helper(nums, i);
        }
        return nums[n - 1];
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    // vector<int> nums = {1, 2, 3, 1};
    // vector<int> nums = {2, 7, 9, 3, 1};
    // vector<int> nums = {};
    // vector<int> nums = {2};
    // vector<int> nums = {2, 7};
    vector<int> nums = {0};
    cout << s.rob(nums);
    return 0;
}
