# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-20 14:11:15
@Last Modified by:   tushushu
@Last Modified time: 2018-11-20 14:11:15
"""

DIC = {i % 26: chr(65 + i) for i in range(26)}


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = []
        while n > 0:
            k = (n - 1) % 26
            ret.append(DIC[k])
            n = (n - 1) // 26
        return ''.join(ret[::-1])
