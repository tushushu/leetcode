#include <string>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution
{
private:
    unordered_map<char, int> _mapping = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}};

public:
    int romanToInt(string s)
    {
        int num = 0;
        string::iterator it;
        string::iterator end = s.end() - 1;
        int ret = _mapping[*end];
        for (it = s.begin(); it != end; ++it)
        {
            num = _mapping[*it];
            if (num < _mapping[*(it + 1)])
            {
                ret -= num;
            }
            else
            {
                ret += num;
            }
        }
        return ret;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.romanToInt("III") << endl;
    cout << s.romanToInt("IV") << endl;
    cout << s.romanToInt("IX") << endl;
    cout << s.romanToInt("LVIII") << endl;
    cout << s.romanToInt("MCMXCIV") << endl;
    string ss = "ABC";
    cout << "end " << *(ss.end()) << endl;
    return 0;
}