# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-12-29 10:20:08
"""
from functools import reduce
MAX = 2**31
MIN = -2**31 - 1


class Solution:
    def helper(self, num):
        if num is 0:
            yield 0
        while num is not 0:
            num, mod = divmod(num, 10)
            yield mod

    def reverse(self, x):
        ret = reduce(lambda x, y: x * 10 + y,
                     self.helper(abs(x))) * [1, -1][x < 0]
        return [0, ret][MIN < ret < MAX]


if __name__ == "__main__":
    t = Solution()
    print(t.reverse(-321))
