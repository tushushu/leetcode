# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-20 14:44:44
"""


class Solution:
    def helper(self, arr):
        yield 1
        ite = iter(arr)
        a = next(ite)
        for b in ite:
            yield a + b
            a = b
        yield 1

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows is 0:
            ret = []
        elif numRows is 1:
            ret = [[1]]
        elif numRows is 2:
            ret = [[1], [1, 1]]
        else:
            ret = [[1], [1, 1]]
            tail = ret[-1]
            for _ in range(numRows - 2):
                tmp = list(self.helper(tail))
                tail = tmp
                ret.append(tail)
        return ret
