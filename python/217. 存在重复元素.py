# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-16 14:58:47
"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique = set()
        for num in nums:
            if num in unique:
                return True
            else:
                unique.add(num)
        return False
