# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 17:54:08 2018

@author: Administrator
"""
class Solution:
    def helper(self, candidates, target, nums):
        if sum(nums) == target:
            return [nums]
        if sum(nums) > target:
            return []
        res = []
        n = len(candidates)
        for i in range(n):
            candidate = candidates[i]
            res.extend(self.helper(candidates[i:], target, nums + [candidate]))
        return res

    def combinationSum(self, candidates, target):
        return self.helper(candidates, target, [])

