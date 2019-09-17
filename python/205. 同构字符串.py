# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-17 14:20:26
"""


class Solution:
    def helper(self, s: str) -> list:
        l = []
        d = dict()
        i = 0
        for c in s:
            if c in d:
                l.append(d[c])
            else:
                d[c] = i
                i += 1
                l.append(d[c])
        return l

    def isIsomorphic(self, s: str, t: str) -> bool:
        l1 = self.helper(s)
        l2 = self.helper(t)
        return len(l1) == len(l2) and all(x == y for x, y in zip(l1, l2))
