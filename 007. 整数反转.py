# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-12-29 10:20:08
"""
MAX = 2**31 - 1
MIN = -2**31


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        digits = []
        if x < 0:
            num = -x
            is_negative = True
        else:
            num = x
            is_negative = False
        while num != 0:
            num, mod = divmod(num, 10)
            digits.append(mod)
        n = len(digits)
        times = 1
        ret = 0
        for i in range(n - 1, -1, -1):
            ret += times * digits[i]
            times *= 10
        if ret > MAX or ret < MIN:
            ret = 0
        else:
            if is_negative:
                ret = -ret
        return ret


if __name__ == "__main__":
    t = Solution()
    print(t.reverse(-321))
