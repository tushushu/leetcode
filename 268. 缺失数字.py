# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-26 10:49:08
"""


class Solution:
    def missingNumber(self, nums: list) -> int:
        return len(nums) + sum(a - b for a, b in enumerate(nums))
