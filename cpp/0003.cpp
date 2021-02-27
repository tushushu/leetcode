#include <string>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        int max_len = 0;
        int current_len = 0;
        int left = 0;
        int right = 0;
        unordered_map<char, int> mapping;
        unordered_map<char, int>::iterator it;
        for (right = 0; right < s.size(); ++right)
        {   
            it = mapping.find(s[right]);
            if (it != mapping.end() && it->second >= left)
            {
                current_len = right - left;
                max_len = current_len > max_len ? current_len : max_len;
                left = it->second + 1;
            }
            mapping[s[right]] = right;
        }
        current_len = right - left;
        return current_len > max_len ? current_len : max_len;
    }
};