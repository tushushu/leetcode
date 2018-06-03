<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 11:07:20 2018

@author: Administrator
"""


class Solution:
    def binSearch(self, nums, target, eq, lt, is_left):
        low = 0
        n = high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if eq(nums, target, mid, n, is_left):
                return mid
            elif lt(nums, target, mid, n, is_left):
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def eq(self, nums, target, i, n, is_left):
        if is_left:
            return (i == 0 or nums[i-1] != target) and nums[i] == target
        else:
            return (i == n or nums[i+1] != target) and nums[i] == target

    def lt(self, nums, target, i, n, is_left):
        return is_left if target == nums[i] else target < nums[i]

    def searchRange(self, nums, target):
        left = self.binSearch(nums, target, self.eq, self.lt, True)
        right = self.binSearch(nums, target, self.eq, self.lt, False)
        return [left, right]
=======
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 11:07:20 2018

@author: Administrator
"""


class Solution:
    def binSearch(self, nums, target, eq, lt, is_left):
        low = 0
        n = high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if eq(nums, target, mid, n, is_left):
                return mid
            elif lt(nums, target, mid, n, is_left):
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def eq(self, nums, target, i, n, is_left):
        if is_left:
            return (i == 0 or nums[i-1] != target) and nums[i] == target
        else:
            return (i == n or nums[i+1] != target) and nums[i] == target

    def lt(self, nums, target, i, n, is_left):
        return is_left if target == nums[i] else target < nums[i]

    def searchRange(self, nums, target):
        left = self.binSearch(nums, target, self.eq, self.lt, True)
        right = self.binSearch(nums, target, self.eq, self.lt, False)
        return [left, right]
>>>>>>> c9978dc9fcf21f5c72e7576e1b249d22946c4f1e
