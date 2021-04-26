#include <vector>
using namespace std;

class Solution
{
public:
    int trap(vector<int> &height)
    {
        int i = 0;
        int result = 0;
        vector<int> left_max(height.size());
        for (i = 1; i < height.size(); ++i)
        {
            left_max[i] = max(left_max[i - 1], height[i - 1]);
        }

        vector<int> right_max(height.size());
        for (i = height.size() - 2; i >= 0; --i)
        {
            right_max[i] = max(right_max[i + 1], height[i + 1]);
        }

        for (i = 0; i < height.size(); ++i)
        {
            result += max(min(left_max[i], right_max[i]) - height[i], 0);
        }
        return result;
    }
};
