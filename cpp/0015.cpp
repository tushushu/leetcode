#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    void twoSum(vector<vector<int>> &ret, vector<int> &nums, int target, int begin)
    {
        int end = nums.size() - 1;
        int tot = 0;
        while (begin < end)
        {
            tot = nums[begin] + nums[end];
            if (tot > target)
            {
                --end;
            }
            else if (tot < target)
            {
                ++begin;
            }
            else
            {
                vector<int> tmp = {-target, nums[begin], nums[end]};
                ret.push_back(tmp);
                while (begin < end && nums[end] == nums[--end])
                    ;
                while (begin < end && nums[begin] == nums[++begin])
                    ;
            }
        }
    }
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        vector<vector<int>> ret;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); ++i)
        {
            if (nums[i] > 0)
            {
                break;
            }
            if (i != 0 && nums[i] == nums[i - 1])
            {
                continue;
            }
            twoSum(ret, nums, -nums[i], i + 1);
        }
        return ret;
    }
};

int main(int argc, const char **argv)
{
    Solution s;
    // vector<int> nums = {3, 1, 2, 2, 3, 3, 4, 2, 1, 4};
    // int target = 5;
    // vector<vector<int>> ret = s.twoSum(nums, target, 2);
    vector<int> nums = {-1, 0, 1, 2, -1, -4};
    vector<vector<int>> ret = s.threeSum(nums);
    for (int i = 0; i < ret.size(); ++i)
    {
        if (nums[i] > 0)
        {
            break;
        }
        for (int j = 0; j < ret[i].size(); ++j)
        {
            cout << ret[i][j] << ",";
        }
        cout << endl;
    }

    return 0;
}