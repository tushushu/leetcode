#include <vector>
#include <unordered_map>
#include <stack>
#include <iostream>
using namespace std;

class Solution
{
public:
    vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
    {
        vector<int> ret(nums1.size(), -1);
        if (nums1.size() < 2)
        {
            return ret;
        }
        unordered_map<int, int> mapping;
        stack<int> elements;
        int i = 0;
        for (i = 0; i < nums1.size(); ++i)
        {
            mapping[nums1[i]] = i;
        }
        for (i = 0; i < nums2.size(); ++i)
        {
            while (!elements.empty() && elements.top() < nums2[i])
            {
                ret[mapping[elements.top()]] = nums2[i];
                elements.pop();
            }
            if (mapping.count(nums2[i]))
            {
                elements.push(nums2[i]);
            }
        }
        return ret;
    }
};

int main(int argc, const char **argv)
{
    int _nums1[2] = {2, 4};
    vector<int> nums1(begin(_nums1), end(_nums1));
    int _nums2[4] = {1, 2, 3, 4};
    vector<int> nums2(begin(_nums2), end(_nums2));
    Solution s;
    s.nextGreaterElement(nums1, nums2);
    return 0;
}