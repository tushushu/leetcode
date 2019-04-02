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
        mid = 0
        width = 0
        is_odd = True
        n = len(s)
        for i in range(n):
            # 奇数
            # 提前终止
            max_len = min(n - 1 - i, i) * 2 + 1
            if max_len > length:
                j = 1
                while i - j >= 0 and i + j < n:
                    if s[i - j] != s[i + j]:
                        break
                    j += 1
                new_len = (j - 1) * 2 + 1
                if new_len >= length:
                    length = new_len
                    mid = i
                    width = j
                    is_odd = True

            # 偶数
            # 提前终止
            j = 0
            max_len = min(n - i, i + 1) * 2
            if max_len > length:
                while i - j >= 0 and i + j + 1 < n:
                    if s[i - j] != s[i + j + 1]:
                        break
                    j += 1
                new_len = j * 2
                if new_len >= length:
                    length = new_len
                    mid = i
                    width = j
                    is_odd = False
        if is_odd:
            ret = s[mid - width + 1: mid + width]
        else:
            ret = s[mid - width + 1: mid + width + 1]
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
