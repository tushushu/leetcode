"""
@Author: tushushu
@Date: 2018-12-25 10:28:49
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        dic = {}
        ret = 0
        start = 0
        n = len(s)
        for end, c in enumerate(s):
            if c in dic and dic[c] >= start:
                ret = max(ret, end - start)
                start = dic[c] + 1
                if n - start < ret:
                    break
            dic[c] = end
        return max(ret, end - start + 1)


if __name__ == "__main__":
    t = Solution()
    s = " "
    print(t.lengthOfLongestSubstring(s))
