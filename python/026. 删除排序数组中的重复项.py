# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-03-11 14:05:52
"""


class Solution:
    def removeDuplicates(self, nums: list) -> int:
        n = len(nums)
        j = 0
        for i in range(1, n):
            if nums[i] == nums[j]:
                pass
            else:
                j += 1
                nums[j] = nums[i]
        return j + 1
