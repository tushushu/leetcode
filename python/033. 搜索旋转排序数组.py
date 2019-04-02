# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-03-13 15:37:36
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
            elif nums[mid] < nums[low]:
                high = mid - 1
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                break
        return -1
