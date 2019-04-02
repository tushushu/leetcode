# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-25 10:27:28
"""


class Solution:
    def plusOne(self, digits):
        flag = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] is 9:
                digits[i] = 0
            else:
                digits[i] += 1
                flag = 0
                break
        if flag is 1:
            return [1] + digits
        else:
            return digits
