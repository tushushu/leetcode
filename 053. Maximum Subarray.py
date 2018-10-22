# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-22 11:01:12
@Last Modified by:   tushushu
@Last Modified time: 2018-10-22 11:01:12
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot_max = -float('inf')
        tot = 0
        for num in nums:
            if tot < 0:
                tot = 0
            tot += num
            if tot > tot_max:
                tot_max = tot
        return tot_max
