#include <iostream>
using namespace std;

class Solution
{
public:
    int reverse(int x)
    {
        long ret = 0;
        while (x)
        {
            ret = ret * 10 + x % 10;
            x /= 10;
        }
        return (ret < INT_MIN || ret > INT_MAX) ? 0 : ret;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    cout << "the result is: " << s.reverse(2147483647) << endl;
    cout << "the result is: " << s.reverse(-2147483648) << endl;
    cout << "the result is: " << s.reverse(-123) << endl;
    cout << "the result is: " << s.reverse(123) << endl;
    cout << "the result is: " << s.reverse(0) << endl;
    return 0;
}
