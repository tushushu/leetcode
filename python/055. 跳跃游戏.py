# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-06-29 20:39:37
@Last Modified by:   tushushu
@Last Modified time: 2021-06-29 20:39:37
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        F(N) -> F(N - i) + num[n - i], if nums[n - i] > i
        """
        i = j = len(nums) - 1
        while j > 0:
            j = j - 1
            if nums[j] + j >= i:
                i = j
        return i == 0
