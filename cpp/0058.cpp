#include <string>
#include <iostream>
using namespace std;

class Solution
{
public:
    int lengthOfLastWord(string s)
    {
        int ret = 0;
        int flag = 0;
        for (string::iterator it = s.begin(); it != s.end(); ++it)
        {
            if (*it != ' ')
            {
                flag ? ++ret : ret = ++flag;
            }
            else
            {
                flag = 0;
            }
        }
        return ret;
    }
};

int main(int argc, char const *argv[])
{
    /* code */
    Solution s;
    cout << s.lengthOfLastWord("") << endl;
    cout << s.lengthOfLastWord(" ") << endl;
    cout << s.lengthOfLastWord("  ") << endl;
    cout << s.lengthOfLastWord("hi") << endl;
    cout << s.lengthOfLastWord(" hi") << endl;
    cout << s.lengthOfLastWord("hi ") << endl;
    cout << s.lengthOfLastWord(" hi ") << endl;
    cout << s.lengthOfLastWord("  hi ") << endl;
    cout << s.lengthOfLastWord(" hi  ") << endl;
    cout << s.lengthOfLastWord("a hi ") << endl;
    cout << s.lengthOfLastWord(" a hi ") << endl;
    cout << s.lengthOfLastWord(" a  hi ") << endl;
    cout << s.lengthOfLastWord(" abc  hi ") << endl;
    return 0;
}
