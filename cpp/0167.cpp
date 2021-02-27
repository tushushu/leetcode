#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        int p = 0;
        int q = numbers.size() - 1;
        vector<int> ret = {0, 0};
        while (1)
        {
            if (numbers[p] + numbers[q] > target)
            {
                --q;
            }
            else if (numbers[p] + numbers[q] < target)
            {
                ++p;
            }
            else
            {
                ret[0] = p + 1;
                ret[1] = q + 1;
                return ret;
            }
        }
    }
};