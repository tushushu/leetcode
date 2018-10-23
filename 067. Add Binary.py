# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-23 10:34:54
@Last Modified by:   tushushu
@Last Modified time: 2018-10-23 10:34:54
"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]
