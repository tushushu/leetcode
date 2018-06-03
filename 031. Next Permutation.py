# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:51:32 2018

@author: Administrator
"""

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        high = n - 1
        i = high - 1
        while nums[i] >= nums[i + 1] and i != -1:
            i -= 1
        target = None if i == -1 else nums[i]
        low = i + 1
        while low <= high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
        if target is not None:
            low = i + 1
            while nums[low] <= target:
                low += 1
            nums[i], nums[low] = nums[low], nums[i]
