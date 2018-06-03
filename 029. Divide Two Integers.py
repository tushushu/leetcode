<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 18:35:03 2018

@author: Administrator
"""


class Solution:
    def __init__(self):
        self.INT_MIN = -2147483648
        self.INT_MAX = 2147483647

    def helper(self, dividend, divisor):
        res = 0
        while dividend >= divisor:
            times = -1
            while (divisor << times + 1) <= dividend:
                times += 1
            res += 1 << times
            dividend -= divisor << times
        return res

    def divide(self, dividend, divisor):
        # cannot use dividend is self.INT_MIN
        if divisor is 0 or (dividend == self.INT_MIN and divisor is -1):
            return self.INT_MAX
        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = self.helper(dividend, divisor)
        return res if positive else -res
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 18:35:03 2018

@author: Administrator
"""


class Solution:
    def __init__(self):
        self.INT_MIN = -2147483648
        self.INT_MAX = 2147483647

    def helper(self, dividend, divisor):
        res = 0
        while dividend >= divisor:
            times = -1
            while (divisor << times + 1) <= dividend:
                times += 1
            res += 1 << times
            dividend -= divisor << times
        return res

    def divide(self, dividend, divisor):
        # cannot use dividend is self.INT_MIN
        if divisor is 0 or (dividend == self.INT_MIN and divisor is -1):
            return self.INT_MAX
        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = self.helper(dividend, divisor)
        return res if positive else -res
>>>>>>> c9978dc9fcf21f5c72e7576e1b249d22946c4f1e
