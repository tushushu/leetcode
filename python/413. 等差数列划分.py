# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-05-02 14:08:00
"""
from typing import List


from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        result = 0
        start = 0
        diff = nums[1] - nums[0]
        i = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != diff:
                if i - start > 2:
                    l = i - start - 2
                    result += (1 + l) * l // 2
                start = i - 1
                diff = nums[i] - nums[start]
        if i - start > 1:
            l = i + 1 - start - 2
            result += (1 + l) * l // 2
        return result
