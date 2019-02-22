# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-22 10:23:38
"""
CACHE = {0: 0, 1: 1}
K = 1


class Solution:
    def fib(self, N: int) -> int:
        global K
        if N <= K:
            return CACHE[N]
        for i in range(K + 1, N + 1):
            CACHE[i] = CACHE[i - 1] + CACHE[i - 2]
        K = N
        return CACHE[N]
