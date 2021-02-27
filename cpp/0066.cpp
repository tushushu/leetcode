#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    vector<int> plusOne(vector<int> &digits)
    {
        vector<int> ret = digits;
        ++ret.back();
        for (int i = ret.size() - 1; i > 0; --i)
        {
            if (ret[i] == 10)
            {
                ret[i] = 0;
                ++ret[i - 1];
            }
        }
        if (ret[0] == 10)
        {
            ret[0] = 0;
            ret.insert(ret.begin(), 1);
        }
        return ret;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> v = {88};
    vector<int> ret = s.plusOne(v);
    for (int i = 0; i < ret.size(); ++i)
    {
        cout << ret[i] << " ";
    }
    return 0;
}
