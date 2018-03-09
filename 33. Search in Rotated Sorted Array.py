# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 18:44:48 2018

@author: Administrator
"""

class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] <= target < nums[mid]:
                high = mid - 1
            elif nums[mid] < target <= nums[high]:
                low = mid + 1
            elif nums[low] > nums[mid]:
                high = mid - 1
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                break
        return -1
