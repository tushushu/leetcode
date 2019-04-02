# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-05 10:45:13
@Last Modified by:   tushushu
@Last Modified time: 2018-11-05 10:45:13
"""


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(map(list, zip(*A)))
