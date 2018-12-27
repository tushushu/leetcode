# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-12-27 21:05:58
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        length = -float("inf")
        ret = ""
        n = len(s)
        for i in range(n):
            print("a", length, ret)
            # 奇数
            j = 1
            while i - j >= 0 and i + j < n:
                if s[i - j] != s[i + j]:
                    break
                j += 1
            if (j - 1) * 2 + 1 >= length:
                length = (j - 1) * 2 + 1
                ret = s[i - j + 1: i + j]
            # 偶数
            j = 0
            while i - j >= 0 and i + j + 1 < n:
                if s[i - j] != s[i + j + 1]:
                    break
                j += 1
            if j * 2 >= length:
                length = j * 2
                ret = s[i - j + 1: i + j + 1]
        return ret


if __name__ == "__main__":
    t = Solution()
    # s = ""
    # print(t.longestPalindrome(s))
    # s = "a"
    # print(t.longestPalindrome(s))
    # s = "ab"
    # print(t.longestPalindrome(s))
    # s = "abba"
    # print(t.longestPalindrome(s))
    s = "ccc"
    print(t.longestPalindrome(s))
