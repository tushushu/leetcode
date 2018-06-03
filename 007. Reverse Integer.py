# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:14:18 2018

@author: Administrator
"""


class Solution:
    def reverse(self, x):
        y = abs(x)
        res = 0
        while y:
            res = res * 10 + y % 10
            y //= 10
        res = -res if x < 0 else res
        return res if (-2**31-1 < res < 2**31) else 0

    def reverse1(self, x):
        sign = lambda x: x and (1, -1)[x < 0]
        r = int(str(sign(x)*x)[::-1])
        return (sign(x)*r, 0)[r > 2**31 - 1]
