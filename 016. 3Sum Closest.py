# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 18:02:51 2018

@author: Administrator
"""


class Solution:
    def binSearch(self, nums, target, low, high, descending):
        if descending:
            if target >= nums[low]:
                return nums[low]
            if target <= nums[high]:
                return nums[high]
            while low <= high:
                mid = (low + high) // 2
                mid_val = nums[mid]
                if mid_val < target:
                    high = mid - 1
                elif mid_val > target:
                    low = mid + 1
                else:
                    return mid_val
        else:
            if target <= nums[low]:
                return nums[low]
            if target >= nums[high]:
                return nums[high]
            while low <= high:
                mid = (low + high) // 2
                mid_val = nums[mid]
                if mid_val < target:
                    low = mid + 1
                elif mid_val > target:
                    high = mid - 1
                else:
                    return mid_val
        low_val = nums[low]
        high_val = nums[high]
        return min(low_val, high_val, key=lambda x: abs(x - target))

    def threeSumClosest(self, nums, target):
        descending = (target < 0)
        nums = sorted(nums, reverse=descending)
        n = len(nums)
        key = float('inf')
        for i in range(n - 2):
            num1 = nums[i]
            for j in range(i + 1, n - 1):
                num2 = nums[j]
                num3 = self.binSearch(nums, target - num2 - num1, j + 1, n - 1, descending)
                tmp = abs(num1 + num2 + num3 - target)
                if tmp < key:
                    key = tmp
                    res = num1 + num2 + num3
                if (num1 + num2) < target < 0 or (num1 + num2) > target > 0:
                    break
        return res
