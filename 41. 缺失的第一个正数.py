# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-03-16 13:22:33
"""


class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        nums1 = [0] * n
        for num in nums:
            if 0 < num <= n:
                nums1[num - 1] = 1
        for i, num in enumerate(nums1):
            if num == 0:
                return i + 1
        return n + 1
        