# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-18 14:12:07
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            if x >= mid * mid and x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                high = mid - 1
            else:
                low = mid + 1


if __name__ == "__main__":
    t = Solution()
    print(t.mySqrt(9))
