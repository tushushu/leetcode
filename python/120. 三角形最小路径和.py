# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-05-05 14:53:39
@Last Modified by:   tushushu
@Last Modified time: 2021-05-05 14:53:39
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        F(N, i) = Min(F(N - 1, i), F(N - 1, i - 1)) + Arr[n][i]
        """
        dp = [[0] * len(triangle[i]) for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        k = 1
        for i in range(1, len(triangle)):
            k += 1
            for j in range(k):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1]
                                   [j - 1]) + triangle[i][j]
        return min(dp[-1])
