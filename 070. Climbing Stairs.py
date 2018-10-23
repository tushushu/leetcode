# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-23 11:05:10
@Last Modified by:   tushushu
@Last Modified time: 2018-10-23 11:05:10
"""


class Solution:
    def helper(self, n, m):
        ret = 1
        for x in range(n - m + 1, n + 1):
            ret *= x
        for x in range(1, m + 1):
            ret /= x
        return ret

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n
        return int(sum(self.helper(n - i, i) for i in range(n // 2 + 1)))
