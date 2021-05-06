# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-05-03 21:59:56
@Last Modified by:   tushushu
@Last Modified time: 2021-05-03 21:59:56
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        F(i) is number of trees when root is i.
        G(n) = F(1) + F(2) + ... + F(n)
        F(i) = G(i - 1) * G(n - i)
        So, G(n) = G(0) * G(n - 1) + G(1) * G(n - 2) + ... + G(n - 1) * G(0)
        """
        if n < 2:
            return 1
        G = [0 for _ in range(n + 1)]
        G[0] = 1
        G[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[-1]
