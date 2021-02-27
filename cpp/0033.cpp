#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    inline int binSearch(vector<int> &nums, int target, int low, int mid, int high)
    {
        while (low <= high)
        {
            mid = (low + high) / 2;
            if (nums[mid] > target)
            {
                high = mid - 1;
            }
            else if (nums[mid] < target)
            {
                low = mid + 1;
            }
            else
            {
                return mid;
            }
        }
        return -1;
    }
    inline int bigSearch(vector<int> &nums, int target, int low, int mid, int high, int n)
    {
        while (low <= high)
        {
            mid = (low + high) / 2;
            if (nums[mid] > target)
            {
                high = mid - 1;
            }
            else if (nums[mid] < target)
            {

                if (nums[mid] >= nums[0])
                {
                    low = mid + 1;
                }
                else
                {
                    high = mid - 1;
                }
            }
            else
            {
                return mid;
            }
        }
        return -1;
    }
    inline int smallSearch(vector<int> &nums, int target, int low, int mid, int high, int n)
    {
        while (low <= high)
        {
            mid = (low + high) / 2;
            if (nums[mid] > target)
            {

                if (nums[mid] <= nums[n])
                {
                    high = mid - 1;
                }
                else
                {
                    low = mid + 1;
                }
            }
            else if (nums[mid] < target)
            {
                low = mid + 1;
            }
            else
            {
                return mid;
            }
        }
        return -1;
    }
    int search(vector<int> &nums, int target)
    {
        if (nums.size() == 0)
        {
            return -1;
        }
        int low = 0;
        int high = nums.size() - 1;
        int mid;
        int n = nums.size() - 1;
        if (nums[0] <= nums[n])
        {
            return binSearch(nums, target, low, mid, high);
        }
        if (target >= nums[0])
        {
            return bigSearch(nums, target, low, mid, high, n);
        }
        if (target <= nums[n])
        {
            return smallSearch(nums, target, low, mid, high, n);
        }
        return -1;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    // vector<int> nums = {1, 2};
    // vector<int> nums = {2, 1};
    // vector<int> nums = {1, 2, 3};
    // vector<int> nums = {2, 3, 1};
    // vector<int> nums = {3, 1, 2};
    // vector<int> nums = {1};
    for (int i = 0; i < nums.size(); ++i)
    {
        cout << s.search(nums, nums[i]) << endl;
    }

    return 0;
}
