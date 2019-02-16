# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-16 15:06:55
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        unique = set()
        for i, num in enumerate(nums):
            if i > k:
                unique.remove(nums[i - k - 1])
            if num in unique:
                return True
            else:
                unique.add(num)
        return False
