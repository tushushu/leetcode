#include <vector>
using namespace std;

class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        if (nums.size() < 2)
        {
            return nums.size();
        }
        int i = 0;
        for (int j = 1; j < nums.size(); j++)
        {
            if (nums[j] != nums[j - 1])
            {
                nums[++i] = nums[j];
            }
        }
        return i + 1;
    }
};