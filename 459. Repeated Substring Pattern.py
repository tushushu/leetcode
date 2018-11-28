# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-27 11:35:30
@Last Modified by:   tushushu
@Last Modified time: 2018-11-27 11:35:30
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        m = n // 2 + 1
        valids = set()
        first = s[0]
        for i, c in enumerate(s):
            if i == 0:
                continue
            if i == m:
                break
            if c == first and n % i == 0:
                valids.add(i)

        for k in valids:
            flag = True
            for i in range(n):
                if s[i] != s[i % k]:
                    flag = False
                    break
            if flag:
                return True
        return False
