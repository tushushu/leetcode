# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-07-12 22:07:33
@Last Modified by:   tushushu
@Last Modified time: 2021-07-12 22:07:33
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        l0 = None
        for i0 in range(n - 3):
            if nums[i0] + nums[i0 + 1] + nums[i0 + 2] + nums[i0 + 3] > target:
                break
            if nums[i0] == l0:
                continue
            l0 = nums[i0]
            l1 = None
            for i1 in range(i0 + 1, n - 2):
                if nums[i0] + nums[i1] + nums[i1 + 1] + nums[i1 + 2] > target:
                    break
                if nums[i1] == l1:
                    continue
                l1 = nums[i1]
                i2 = i1 + 1
                i3 = n - 1
                while i2 < i3:
                    tot = nums[i0] + nums[i1] + nums[i2] + nums[i3]
                    if tot > target:
                        i3 -= 1
                    elif tot < target:
                        i2 += 1
                    else:
                        result.append([nums[i0], nums[i1], nums[i2], nums[i3]])
                        while i2 < i3 and nums[i2] == nums[i2 + 1]:
                            i2 += 1
                        i2 += 1
                        while i2 < i3 and nums[i3] == nums[i3 - 1]:
                            i3 -= 1
                        i3 -= 1
        return result
