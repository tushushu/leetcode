# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:46:06 2018

@author: Administrator
"""

class Solution:
    def partition(self, nums, l, r):  
        x = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= x:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def quick_sort(self, nums, l, r):  
        if l < r:
            q = self.partition(nums, l, r)
            self.quick_sort(nums, l, q - 1)
            self.quick_sort(nums, q + 1, r)

    def _combinationSum2(self, candidates, target, nums):
        if sum(nums) == target:
            return [nums]
        if sum(nums) > target:
            return []
        res = []
        for i, candidate in enumerate(candidates):
            if i == 0 or candidate != candidates[i - 1]:
                res.extend(self._combinationSum2(candidates[i + 1:], target, nums + [candidate]))
        return res

    def combinationSum2(self, candidates, target):
        l = 0
        r = len(candidates) - 1
        self.quick_sort(candidates, l, r)
        return self._combinationSum2(candidates, target, [])

test = Solution()
test.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
