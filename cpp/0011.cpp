#include <vector>
using namespace std;

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int p = 0;
        int q = height.size() - 1;
        int ret = min(height[p], height[q]) * (q - p);
        while (p < q)
        {
            height[p] < height[q] ? ++p : --q;
            ret = max(ret, min(height[p], height[q]) * (q - p));
        }
        return ret;
    }
};