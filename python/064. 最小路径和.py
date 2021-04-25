# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-04-10 15:44:40
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j == 0:
                        dp[i][j] = grid[i][j]
                    else:
                        dp[i][j] = dp[i][j - 1] + grid[i][j]
                else:
                    if j == 0:
                        dp[i][j] = dp[i - 1][j] + grid[i][j]
                    else:
                        dp[i][j] = min(dp[i][j - 1] + grid[i][j],
                                       dp[i - 1][j] + grid[i][j])
        return dp[i][j]
