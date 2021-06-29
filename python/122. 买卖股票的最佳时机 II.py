# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-06-29 20:48:44
@Last Modified by:   tushushu
@Last Modified time: 2021-06-29 20:48:44
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot = 0
        buy = sell = prices[0]
        for price in prices:
            if price < sell:
                tot += sell - buy
                buy = price
            sell = price
        tot += sell - buy
        return tot
