#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        int i;
        int j = 0;
        int n = strs.size();
        if (n == 0)
        {
            return "";
        }
        while (1)
        {
            for (i = 0; i < n; ++i)
            {
                if (j >= strs[i].size() || strs[i][j] != strs[0][j])
                {
                    return strs[0].substr(0, j);
                }
            }
            ++j;
        }
        return strs[0].substr(0, j);
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<string> strs;
    strs = {"flower", "flow", "flight"};
    cout << s.longestCommonPrefix(strs) << endl;
    strs = {"flow", "flow"};
    cout << s.longestCommonPrefix(strs) << endl;
    strs = {"fl", "ab"};
    cout << s.longestCommonPrefix(strs) << endl;
    strs = {"flow", "ab"};
    cout << s.longestCommonPrefix(strs) << endl;
    strs = {};
    cout << s.longestCommonPrefix(strs) << endl;
    return 0;
}
