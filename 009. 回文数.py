# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-05 17:35:43
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        nums = []
        while x != 0:
            x, num = divmod(x, 10)
            nums.append(num)
        n = len(nums)
        for i in range(n//2):
            if nums[i] != nums[n - i - 1]:
                return False
        return True
