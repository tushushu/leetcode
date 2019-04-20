# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-04-10 15:44:40
"""


class Solution:
    def minPathSum(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        ret = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                

if __name__ == "__main__":
    t = Solution()
    # grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    grid = []
    t.minPathSum(grid)
