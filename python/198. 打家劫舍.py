# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-06-27 22:18:43
@Last Modified by:   tushushu
@Last Modified time: 2021-06-27 22:18:43
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        F(N) = max(F(N-1), F(N-2)) + f(N)
        """
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2]+ nums[i])
        return dp[-1]
