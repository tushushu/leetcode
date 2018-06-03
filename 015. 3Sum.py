# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:20:44 2018

@author: Administrator
"""


class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        n = len(nums)
        res = []
        last_left = float('inf')
        i = 0
        while i < n - 1 and nums[i] <= 0:
            left = nums[i]
            if left == last_left:
                i += 1
                continue
            dic = {}
            max_right = -(left + nums[i + 1])
            last_mid = float('inf')
            last_right = float('inf')
            j = i + 1

            while j < n and nums[j] <= max_right:
                mid = right = nums[j]
                if right >= 0 and right != last_right and right in dic:
                    val = dic[right]
                    res.append([val, -(right + val), right])
                    last_right = right
                if left + mid <= 0 and mid != last_mid:
                    key = -(left + mid)
                    dic[key] = left
                    last_mid = mid
                j += 1

            last_left = left
            i += 1
        return res
