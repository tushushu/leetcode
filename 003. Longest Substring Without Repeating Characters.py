# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 18:28:19 2018

@author: Administrator
"""
import numpy as np


class Solution:
    def lengthOfLongestSubstring(self, s):
        if s is "":
            return 0
        dic = {}
        res = start = 0
        for i, char in enumerate(s):
            if char in dic:
                j = dic[char]
                if j >= start:
                    res = max(res, i - start)
                    start = j + 1
            dic[char] = i
        res = max(res, i + 1 - start)
        return res
