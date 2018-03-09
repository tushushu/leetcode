# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:14:07 2018

@author: Administrator
"""


class Solution:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        if not nums:
            return 0
        if target < nums[low]:
            return low
        if target > nums[high]:
            return high + 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low
