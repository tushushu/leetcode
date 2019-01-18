# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-18 11:16:31
"""


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict()
        arr1 = []
        arr2 = []
        i = 0
        for j, c in enumerate(s):
            if c in dic:
                arr1[dic[c]] += 1
            else:
                dic[c] = i
                arr1.append(1)
                arr2.append(j)
                i += 1
        try:
            ret = arr2[arr1.index(1)]
        except ValueError:
            ret = -1
        return ret
