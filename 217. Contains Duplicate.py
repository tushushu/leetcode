# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-26 18:31:47
@Last Modified by:   tushushu
@Last Modified time: 2018-11-26 18:31:47
"""


class Solution(object):
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
