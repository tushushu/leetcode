# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 19:01:48 2018

@author: Administrator
"""


class Solution:
    def helper(self, s):
        cmp = ''
        res = []
        for char in s:
            if char == cmp:
                res[-2] += 1
            else:
                res.extend([1, char])
                cmp = char
        return ''.join(map(str, res))

    def countAndSay(self, n):
        res = '1'
        for _ in range(n-1):
            res = self.helper(res)
        return res
