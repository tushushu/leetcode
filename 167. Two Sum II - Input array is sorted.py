# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-19 15:47:22
@Last Modified by:   tushushu
@Last Modified time: 2018-11-19 15:47:22
"""


class Solution(object):
    def binSearch(self, numbers, target, low, high, exact=True):
        while low <= high:
            mid = (low + high) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return None if exact else min(low, len(numbers) - 1)

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        high = self.binSearch(
            numbers, target - numbers[0], 0, len(numbers)-1, False)
        half_target = target // 2

        for i, a in enumerate(numbers):
            if a > half_target:
                break
            j = self.binSearch(numbers, target-a, i+1, high)
            if j:
                return [i + 1, j + 1]
