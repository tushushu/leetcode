# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-04-28 18:58:48
@Last Modified by:   tushushu
@Last Modified time: 2021-04-28 18:58:48
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        result = 0
        current_min = prices[0]
        for p in prices:
            current_min = min(p, current_min)
            result = max(p - current_min, result)
        return result
