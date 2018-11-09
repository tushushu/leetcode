# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-09 10:37:10
@Last Modified by:   tushushu
@Last Modified time: 2018-11-09 10:37:10
"""


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[0::2])
