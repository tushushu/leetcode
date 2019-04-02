# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-14 11:53:43
"""


class Solution:
    def helper(self, s, n, k):
        for i in range(0, n, k):
            yield s[i:i + k]

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(n // 2):
            if n % (i + 1):
                pass
            else:
                if all(x == s[:i + 1] for x in
                       self.helper(s, n, i + 1)):
                    return True
        return False
