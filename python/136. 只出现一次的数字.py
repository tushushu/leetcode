# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-04 10:56:37
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            print(ret)
            ret ^= num
        print(ret)
        return ret


if __name__ == "__main__":
    t = Solution()
    nums = [1, 2, 3, 2, 1, 3, 4, 5, 6, 4, 6]
    t.singleNumber(nums)
