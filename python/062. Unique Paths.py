# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-12-13 15:43:30
@Last Modified by:   tushushu
@Last Modified time: 2018-12-13 15:43:30
"""


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[1] * m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]


if __name__ == "__main__":
    t = Solution()
    print(t.uniquePaths(10, 10))
