#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{
  public:
    int lengthOfLongestSubstring(string s)
    {
        // 变量声明
        int ret = 0;
        int start = 0;
        int end = 0;
        int n = s.length();
        char c;
        unordered_map<char, int> mapping;

        // 提前终止
        if (n == 0)
        {
            return ret;
        }

        // 滑动窗口
        while (end < n)
        {
            c = s[end];
            if (mapping.find(c) != mapping.end() && mapping[c] >= start)
            {
                ret = max(ret, end - start);
                start = mapping[c] + 1;
                if (n - start < ret)
                {
                    ret = max(ret, end - start);
                    break;
                }
            }
            mapping[c] = end;
            end++;
        }
        ret = max(ret, end - start);
        return ret;
    }
};