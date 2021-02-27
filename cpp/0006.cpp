#include <string>
#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    string convert(string s, int numRows)
    {
        if (numRows == 1){
            return s;
        }
        vector<string> newStrs(numRows, "");
        int row = 0;
        int inc = 1;
        for (int i = 0; i < s.size(); ++i)
        {
            newStrs[row].push_back(s[i]);
            if (row == numRows - 1){
                inc = -1;
            }else if (row == 0){
                inc = 1;
            }
            row += inc;
        }
        string ret = "";
        for (int i = 0; i < newStrs.size(); ++i)
        {
            ret += newStrs[i];
        }
        return ret;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.convert("", 0) << endl;
    cout << s.convert("abc", 1) << endl;
    cout << s.convert("PAYPALISHIRING", 3) << endl;
    return 0;
}
