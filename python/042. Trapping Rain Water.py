# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-04-25 10:03:52
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        for i in range(n - 1):
            if height[i] > max_left[i]:
                max_left[i + 1] = height[i]
            else:
                max_left[i + 1] = max_left[i]

        max_right = [0] * n
        for i in range(n - 1, 0, -1):
            if height[i] > max_right[i]:
                max_right[i - 1] = height[i]
            else:
                max_right[i - 1] = max_right[i]

        water = 0
        for i in range(n):
            water += max(min(max_left[i], max_right[i]) - height[i], 0)
        return water
