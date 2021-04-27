# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-04-27 21:22:52
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(s)
        for c in t:
            if i == n:
                return True
            if s[i] == c:
                i += 1
        return False
