# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:47:58 2018

@author: Administrator
"""


STR2INT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
RULE = {'I': {'V', 'X'}, 'X': {'L', 'C'}, 'C': {'D', 'M'}}


class Solution:
    def romanToInt(self, s):
        ite = iter(s[::-1])
        a = next(ite)
        ret = STR2INT[a]
        for b in ite:
            if RULE.get(b) and a in RULE[b]:
                ret -= STR2INT[b]
            else:
                ret += STR2INT[b]
            a = b
        return ret
