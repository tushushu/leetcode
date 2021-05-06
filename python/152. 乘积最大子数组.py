# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-05-06 18:08:18
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        F(n) = F(n - 1) * arr[n]
        """
        pos = [-1] * len(nums)
        neg = [1] * len(nums)
        if nums[0] > 0:
            pos[0] = nums[0]
        else:
            neg[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos[i] = max(nums[i] * pos[i - 1], nums[i])
                neg[i] = nums[i] * neg[i - 1]
            else:
                neg[i] = min(nums[i] * pos[i - 1], nums[i])
                pos[i] = nums[i] * neg[i - 1]
        res = max(pos)
        if res < 0:
            res = max(nums)
        return res
