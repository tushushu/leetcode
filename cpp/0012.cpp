#include <string>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<vector<string>> mapping = {
        {"", "I", "II", "IV", "V", "VI", "VII", "VIII", "IX"},
        {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"},
        {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"},
        {"", "M", "MM", "MMM", "", "", "", "", "", ""}
    };

    string intToRoman(int num)
    {
        string ret= "";
        int i = 3;
        while (num)
        {
            ret = mapping[3 - i][num % 10] + ret;
            num /= 10;
            --i;
        }
        return ret;
    }
};