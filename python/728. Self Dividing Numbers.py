# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-31 10:40:00
@Last Modified by:   tushushu
@Last Modified time: 2018-10-31 10:40:00
"""


class Solution:
    def helper(self, num):
        num_copy = num
        while num_copy:
            digit = num_copy % 10
            if digit == 0 or num % digit != 0:
                return False
            num_copy //= 10
        return True

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return list(filter(self.helper, range(left, right + 1)))
