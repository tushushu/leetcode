#include <vector>
using namespace std;

class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int i = -1;
        vector<int>::iterator it = nums.begin();
        vector<int>::iterator end = nums.end();
        for (; it != end; ++it)
        {
            if (*it != val)
            {
                nums[++i] = *it;
            }
        }
        return i + 1;
    }
};