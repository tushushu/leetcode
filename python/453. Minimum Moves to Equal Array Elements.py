# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-07 10:30:04
@Last Modified by:   tushushu
@Last Modified time: 2018-11-07 10:30:04
"""


class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)
