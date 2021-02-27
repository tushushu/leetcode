#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        vector<int> ret = {-1, -1};
        int low = 0;
        int high = nums.size() - 1;
        if (high == -1 || target < nums[0] || target > nums[high]){
            return ret;
        }
        int mid;
        int min_high = high;
        int max_low = low;
        nums.push_back(INT_MAX);
        while (low <= high)
        {
            mid = (low + high) / 2;
            if (mid > 0 && nums[mid - 1] >= target)
            {
                high = mid - 1;
                if (nums[high] > target){
                    min_high = high;
                }
                if (nums[high] == target){
                    max_low = high;
                }
            }
            else
            {
                if (nums[mid] == target)
                {
                    ret[0] = mid;
                    break;
                }
                else
                {
                    low = mid + 1;
                }
            }
        }
        if (ret[0] == -1)
        {
            return ret;
        }
        high = min_high;
        low = max(mid, max_low);
        while (low <= high)
        {
            mid = (low + high) / 2;
            if (nums[mid + 1] <= target)
            {
                low = mid + 1;
            }
            else
            {
                if (nums[mid] == target)
                {

                    ret[1] = mid;
                    break;
                }
                else
                {
                    high = mid - 1;
                }
            }
        }
        return ret;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> nums = {5, 7, 7, 8, 8, 10};
    // vector<int> nums = {};
    // vector<int> nums = {1};
    // vector<int> nums = {5};
    int target = 5;
    vector<int> result;
    result = s.searchRange(nums, target);
    cout << "target " << target << " ret " << result[0] << " " << result[1] << endl;
    return 0;
}
