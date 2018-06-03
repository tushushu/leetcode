# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:14:46 2018

@author: Administrator
"""


class Solution:
    def getArea(self, height, i, j):
        return (j - i) * min(height[i], height[j])

    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        res = self.getArea(height, i, j)
#        print(i, j)
        while i < j:
            if height[i] < height[j]:
                i += 1
                update = height[i] > height[i - 1]
            else:
                j -= 1
                update = height[j] > height[j + 1]
            if update:
                res = max(res, self.getArea(height, i, j))
#            print(i, j)
        return res
