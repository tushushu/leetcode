# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-05-16 16:51:32
@Last Modified by:   tushushu
@Last Modified time: 2021-05-16 16:51:32
"""
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        F(n) = Min(F(n - 1) + cost[n - 1], F(n - 2) + cost[n - 2])
        """
        if len(cost) == 2:
            return min(cost)
        dp = [0 for _ in range(len(cost) + 1)]
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]
