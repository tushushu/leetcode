# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-17 14:29:07
"""


class Solution:
    def helper(self, num):
        ret = 0
        num1 = num
        while num1:
            num1, num2 = divmod(num1, 10)
            ret += num2 ** 2
        return ret

    def isHappy(self, n: int) -> bool:
        ret = n
        unique = set([n])
        while ret != 1:
            ret = self.helper(ret)
            if ret in unique:
                return False
            unique.add(ret)
        return True
