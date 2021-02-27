#include <string>
#include <unordered_map>
#include <unordered_set>
#include <stack>
using namespace std;

class Solution
{
private:
    unordered_map<char, char> _pairs = {
        {'{', '}'},
        {'[', ']'},
        {'(', ')'}};
    unordered_set<char> _left = {'{', '[', '('};

public:
    bool isValid(string s)
    {
        stack<char> brackets;
        int n = s.size();
        for (int i = 0; i < n; ++i)
        {
            if (brackets.size() > n - i)
            {
                return false;
            }
            if (_left.count(s[i]))
            {
                brackets.push(s[i]);
            }
            else
            {
                if (!brackets.empty() && _pairs.at(brackets.top()) == s[i])
                {
                    brackets.pop();
                }
                else
                {
                    return false;
                }
            }
        }
        return brackets.empty();
    }
};