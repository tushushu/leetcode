# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:14:06 2018

@author: Administrator
"""


class Solution:
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
