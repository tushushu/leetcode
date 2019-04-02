# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-22 10:26:04
@Last Modified by:   tushushu
@Last Modified time: 2018-11-22 10:26:04
"""
DIC = {chr(64 + i): i for i in range(1, 27)}


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = 1
        ret = 0
        for c in s[::-1]:
            ret += DIC[c] * k
            k *= 26
        return ret
