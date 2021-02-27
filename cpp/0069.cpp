#include <iostream>
using namespace std;

class Solution
{
public:
    int mySqrt(int x)
    {
        long low = 0;
        long high = x;
        long mid = 0;
        while (low <= high)
        {
            mid = (low + high) / 2;
            if (mid * mid > x)
            {
                high = mid - 1;
            }
            else if ((mid + 1) * (mid + 1) <= x)
            {
                low = mid + 1;
            }
            else
            {
                break;
            }
        }
        return mid;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    for (int x = 0; x < 10; ++x)
    {
        cout << "x is " << x << " sqrt is " << s.mySqrt(x) << endl;
    }
    cout << "x is " << 1073697799 << " sqrt is " << s.mySqrt(1073697799) << endl;

    return 0;
}
