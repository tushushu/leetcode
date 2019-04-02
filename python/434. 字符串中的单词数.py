# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-11 19:19:35
"""


class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        ret = 0
        flag = False
        for c in s:
            if c is " ":
                if flag:
                    ret += 1
                    flag = False
            else:
                if not flag:
                    flag = True
        else:
            if flag:
                ret += 1
        return ret
