# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-01 10:42:38
@Last Modified by:   tushushu
@Last Modified time: 2018-11-01 10:42:38
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for num in nums:
            ret ^= num
        return ret
