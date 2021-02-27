#include <string>
#include <vector>
using namespace std;

class Solution
{
public:
    bool helper(vector<char> &s, int mid, int max_len)
    {
        int left = mid - 1 - max_len;
        int right = mid + 1 + max_len;
        return left >= 0 && right < s.size() && s[left] == s[right];
    }
    string longestPalindrome(string s)
    {
        vector<char> new_str(s.size() * 2 + 1, '#');
        for (int i = 0; i < s.size(); ++i)
        {
            new_str[i * 2 + 1] = s[i];
        }

        vector<int> max_lengths(new_str.size(), 0); // Array to record longest palindrome
        int center = 0, boundary = 0, max_len = 0, result_center = 0;
        for (int i = 1; i < new_str.size(); ++i)
        {
            if (boundary > i)
            {
                max_lengths[i] = min(boundary - i, max_lengths[center - (i - center)]); // shortcut
            }
            else
            {
                max_lengths[i] = 0;
            }

            while (helper(new_str, i, max_lengths[i])) // Attempt to expand palindrome centered at i
            {
                max_lengths[i]++;
            }

            if (i + max_lengths[i] > boundary)
            { // update center and boundary
                center = i;
                boundary = i + max_lengths[i];
            }
            if (max_lengths[i] > max_len)
            { // update result
                max_len = max_lengths[i];
                result_center = i;
            }
        }
        return s.substr((result_center - max_len) / 2, max_len);
    }
};