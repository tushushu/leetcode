# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:44:48 2018

@author: Administrator
"""


class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for idx, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], idx]
            else:
                dic[num] = idx
