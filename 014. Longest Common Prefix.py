# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:04:43 2018

@author: Administrator
"""


class Solution:
    def helper(self, strs, i, s):
        res = True
        for str_ in strs:
            if str_[:i] != s:
                res = False
                break
        return res

    def longestCommonPrefix(self, strs):
        s = strs[0] if strs else ''
        n = len(s)
        res = ''
        for i in range(1, n+1):
            si = s[:i]
            if self.helper(strs, i, si):
                res = max(res, si, key=len)
        return res
