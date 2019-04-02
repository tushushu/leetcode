# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-11 15:12:02
"""


class Solution:
    def removeElement(self, nums, val):
        i = 0
        for num in nums:
            if num is val:
                pass
            else:
                nums[i] = num
                i += 1
        return i
