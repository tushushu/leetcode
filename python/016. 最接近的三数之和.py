# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-07-10 17:04:11
@Last Modified by:   tushushu
@Last Modified time: 2021-07-10 17:04:11
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        diff = abs(result - target)
        for i in range(len(nums) - 2):
            p = i + 1
            q = len(nums) - 1
            while p < q:
                _result = nums[i] + nums[p] + nums[q]
                _diff = abs(_result - target)
                if _diff < diff:
                    diff = _diff
                    result = _result
                if _result > target:
                    q -= 1
                elif _result < target:
                    p += 1
                else:
                    break
        return result
