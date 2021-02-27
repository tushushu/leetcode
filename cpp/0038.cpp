#include <string>
#include <iostream>
using namespace std;

class Solution
{
public:
    string helper(string &s)
    {
        string ret = "";
        char last = s[0];
        char cnt = 48;
        for (string::iterator it = s.begin(); it != s.end(); ++it)
        {
            if (*it == last)
            {
                cnt += 1;
            }
            else
            {
                ret += cnt;
                ret += last;
                cnt = 49;
            }
            last = *it;
        }
        ret += cnt;
        ret += last;
        return ret;
    }
    string countAndSay(int n)
    {
        string ret = "1";
        for (; n > 1; --n)
        {
            ret = helper(ret);
        }
        return ret;
    }
};

int main(int argc, char const *argv[])
{
    /* code */
    Solution ss;
    string s = "312211";
    cout << ss.helper(s) << endl;
    return 0;
}
