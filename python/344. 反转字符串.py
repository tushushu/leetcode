# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-09 14:27:57
"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ret = []
        for i in range(n):
            ret.append(s[n - i - 1])
        return "".join(ret)
