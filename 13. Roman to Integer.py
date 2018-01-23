# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:47:58 2018

@author: Administrator
"""


class Solution:
    def __init__(self):
        self.dic = {'I': 1, 'X': 10, 'C': 100, 'M': 1000, 'V': 5, 'L': 50, 'D': 500}

    def romanToInt(self, s):
        res = 0
        last_val = -1
        for char in s[::-1]:
            val = self.dic[char]
            res += [1, -1][int(val < last_val)] * val
            last_val = val
        return res
