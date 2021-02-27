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
        vector<int> ret;
        int n = nums.size();
        unordered_map<int, int>::iterator it;
        for (int i = 0; i < n; i++)
        {
            it = mapping.find(nums[i]);
            if (it != mapping.end())
            {
                ret.push_back(i);
                ret.push_back(it->second);
                break;
            }
            else
            {
                mapping[target - nums[i]] = i;
            }
        }
        return ret;
    }
};