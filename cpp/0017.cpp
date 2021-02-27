#include <string>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<string> helper(string s, vector<string> svec)
    {
        vector<string> ret;
        for (int i = 0; i < svec.size(); ++i)
        {
            for (int j = 0; j < s.size(); ++j)
            {
                ret.push_back(svec[i] + s[j]);
            }
        }
        return ret;
    }
    vector<string> letterCombinations(string digits)
    {
        vector<string> ret;
        if (digits == "")
        {
            return ret;
        }
        ret.push_back("");
        vector<string> mapping = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        string s;
        for (int i = 0; i < digits.size(); ++i)
        {
            s = mapping[digits[i] - 50];
            ret = helper(s, ret);
        }
        return ret;
    }
};