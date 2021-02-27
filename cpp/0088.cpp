#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        for (; m && n; nums1[m + n] = nums1[m - 1] > nums2[n - 1] ? nums1[--m] : nums2[--n]);
        for (; n; nums1[m + n] = nums2[--n]);
    }
};