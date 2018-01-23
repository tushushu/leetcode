# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 09:59:51 2018

@author: Administrator
"""
import re


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        p = re.compile("^\s*(\+?|-?)\d+")
        try:
            res = int(p.match(str).group().replace(' ', ''))
        except:
            res = 0
        return max(INT_MIN, min(INT_MAX, res))
