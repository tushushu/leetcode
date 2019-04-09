#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution
{
  public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> mapping;
        // map<int, int> mapping;
        vector<int> ret;
        int n = nums.size();
        int val;
        for (int i = 0; i < n; i++)
        {
            if (mapping.find(nums[i]) != mapping.end())
            {
                ret.push_back(i);
                ret.push_back(mapping[nums[i]]);
                break;
            }
            else
            {
                val = target - nums[i];
                mapping[val] = i;
            }
        }

        return ret;
    }
};

int main(int argc, char const *argv[])
{
    int arr[] = {2, 7, 11, 15};
    int n = sizeof(arr) / sizeof(int);
    int target = 9;
    vector<int> nums(arr, arr + n);
    Solution s;
    vector<int> ret = s.twoSum(nums, target);
    cout << "结果是: ";
    for (int i = 0; i < ret.size(); i++)
    {
        cout << i << ',';
    }

    return 0;
}