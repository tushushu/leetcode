# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-05-16 16:53:48
@Last Modified by:   tushushu
@Last Modified time: 2021-05-16 16:53:48
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        F(n) means max sub array nums[n] is used.
        IF F(n - 1) <= 0: F(n) = nums[n]
        ELSE: F(n) = F(n - 1) + nums[n]
        """
        dp = [x for x in nums]
        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] += dp[i - 1]
        return max(dp)
