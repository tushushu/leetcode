#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int largestPerimeter(vector<int> &A)
    {
        if (A.size() < 3)
        {
            return 0;
        }
        sort(A.begin(), A.end(), greater<int>());
        int i = 0;
        int n = A.size() - 2;
        for (i = 0; i < n; ++i)
        {
            if (A[i] < A[i + 1] + A[i + 2])
            {
                return A[i] + A[i + 1] + A[i + 2];
            }
        }
        return 0;
    }
};
