# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-12 15:00:18
"""
from typing import List


class Solution:
    def helper(self, target: int, nums: List[int], k: int):
        n = len(nums)
        tot = sum(nums[:k])
        if tot >= target:
            return True
        for i in range(n - k):
            tot += (nums[i + k]) - nums[i]
            if tot >= target:
                return True
        return False

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        low = 1
        high = len(nums)
        ret = high + 1
        while low <= high:
            mid = (low + high) // 2
            if self.helper(target, nums, mid):
                ret = min(mid, ret)
                high = mid - 1
            else:
                low = mid + 1
        return 0 if ret > len(nums) else ret
