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
        int n = s.length();
        char c;
        unordered_map<char, int> mapping;

        // 提前终止
        if (n == 0)
        {
            return ret;
        }

        // 滑动窗口
        for (int end = 0; end < n; end++)
        {
            c = s[end];
            if (mapping.find(c) != mapping.end() && mapping[c] >= start)
            {
                ret = max(ret, end - start);
                start = mapping[c] + 1;
                if (n - start < ret)
                {
                    ret = max(ret, end - start + 1);
                    break;
                }
            }
            mapping[c] = end;
        }
        return ret;
    }
};