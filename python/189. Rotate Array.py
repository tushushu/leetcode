# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-21 11:34:06
@Last Modified by:   tushushu
@Last Modified time: 2018-11-21 11:34:06
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        m = n - k
        for _ in range(m):
            nums.append(nums.pop(0))
