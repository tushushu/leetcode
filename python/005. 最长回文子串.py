# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-05-05 16:13:24
@Last Modified by:   tushushu
@Last Modified time: 2021-05-05 16:13:24
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        i: left
        j: right
        F(i, j) = F(i + 1, j - 1) AND s[i] == s[j]
        But it's hard to update, when using for loop i(for loop j).

        Another form,
        l: length
        i: index
        F(i, l) = F(i + 1, l - 2) AND s[i] == s[i + l - 1]
        """
        if len(s) < 2:
            return s
        dp = [[True if l == 0 else False] * len(s) for l in range(len(s) + 1)]
        start, end = 0, 1
        max_len = 0
        for l in range(1, len(s) + 1):
            for i in range(len(s) - l + 1):
                if l < 2:
                    dp[l][i] = True
                else:
                    dp[l][i] = dp[l - 2][i + 1] and s[i] == s[i + l - 1]
                if dp[l][i] and l > max_len:
                    start, end = i, i + l
                    max_len = l
        return s[start:end]
