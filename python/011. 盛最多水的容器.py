# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-05 17:35:43
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p = ret = 0
        q = len(height) - 1
        while p is not q:
            ret = max(ret, min(height[p], height[q]) * (q - p))
            if height[p] < height[q]:
                p += 1
            else:
                q -= 1
        return ret
