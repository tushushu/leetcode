# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:47:58 2018

@author: Administrator
"""


DIC = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class Solution:
    def romanToInt(self, s):
        ite = iter(s[::-1])
        a = next(ite)
        ret = DIC[a]
        for b in ite:
            c1 = b is 'I' and a in ('V', 'X')
            c2 = b is 'X' and a in ('L', 'C')
            c3 = b is 'C' and a in ('D', 'M')
            if c1 or c2 or c3:
                ret -= DIC[b]
            else:
                ret += DIC[b]
            a = b
        return ret
