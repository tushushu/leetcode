# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-04-28 19:23:03
@Last Modified by:   tushushu
@Last Modified time: 2021-04-28 19:23:03
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy1 = -prices[0]
        sell1 = 0
        buy2 = buy1
        sell2 = sell1
        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, buy1 + p)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, buy2 + p)
        return sell2
