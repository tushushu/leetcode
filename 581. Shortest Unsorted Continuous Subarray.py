# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-12-04 11:29:50
@Last Modified by:   tushushu
@Last Modified time: 2018-12-04 11:29:50
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = sorted(nums)
        n = len(nums)
        start = -1
        for a, b in zip(arr, nums):
            if a != b:
                break
            else:
                start += 1
        if start == n - 1:
            return 0
        end = n
        for a, b in zip(arr[::-1], nums[::-1]):
            if a != b:
                break
            else:
                end -= 1

        return end - start - 1
