# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-03 10:23:02
"""
from itertools import cycle


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 1 or s == "":
            return s
        ite = cycle([1] * k + [0] * k)
        stack = []
        ret = []
        for i, c in enumerate(s):
            cond = next(ite)
            if cond:
                stack.append(c)
            else:
                if stack:
                    while stack:
                        ret.append(stack.pop())
                ret.append(c)
        if stack:
            while stack:
                ret.append(stack.pop())
        return "".join(ret)
