#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution
{
public:
    inline int indexVector(vector<int> nums, int i)
    {
        if (i == -1)
        {
            return INT_MIN;
        }
        if (i == nums.size())
        {
            return INT_MAX;
        }
        return nums[i];
    }
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        if (nums1.size() > nums2.size())
        {
            swap(nums1, nums2);
        }
        int low = -1;
        int high = nums1.size();
        int index1, index2;
        double ret;
        while (low <= high)
        {
            index1 = (low + high) / 2;
            index2 = (nums1.size() + nums2.size()) / 2 - index1 - 2;
            if (indexVector(nums1, index1) > indexVector(nums2, index2 + 1))
            {
                high = index1 - 1;
            }
            else if (indexVector(nums2, index2) > indexVector(nums1, index1 + 1))
            {
                low = index1 + 1;
            }
            else
            {
                break;
            }
        }
        ret = min(indexVector(nums1, index1 + 1), indexVector(nums2, index2 + 1));
        if ((nums1.size() + nums2.size()) % 2 == 0)
        {
            ret += max(indexVector(nums1, index1), indexVector(nums2, index2));
            ret /= 2;
        }
        return ret;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> nums1 = {1, 2};
    vector<int> nums2 = {};
    cout << s.findMedianSortedArrays(nums1, nums2);
    return 0;
}
