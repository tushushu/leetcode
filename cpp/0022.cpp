#include <string>
#include <vector>
#include <iostream>
using namespace std;

class Solution
{
private:
    void _helper(vector<string> &ret, string s, int n, int l, int r)
    {
        if (r + l == 2 * n)
        {
            ret.push_back(s);
            return;
        }
        if (l > r)
        {
            _helper(ret, s + ")", n, l, r + 1);
        }
        if (l != n)
        {
            _helper(ret, s + "(", n, l + 1, r);
        }
    }

public:
    vector<string> generateParenthesis(int n)
    {
        vector<string> ret;
        _helper(ret, "", n, 0, 0);
        return ret;
    }
};