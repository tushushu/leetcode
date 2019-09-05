# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-05 14:46:40
"""
from typing import List


class Solution:
    def partition(self, arr, low, high):
        i = low - 1
        for j in range(low, high):
            if arr[j] > arr[high]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[high], arr[i + 1] = arr[i + 1], arr[high]
        return i + 1

    def _findKthLargest(self, nums: List[int], k: int, low: int, high: int):
        if low == high:
            return nums[low]
        mid = self.partition(nums, low, high)
        if k == mid:
            ret = nums[mid]
        elif k < mid:
            ret = self._findKthLargest(nums, k, low, mid - 1)
        else:
            ret = self._findKthLargest(nums, k, mid + 1, high)
        return ret

    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k < 1 or k > len(nums):
            return None
        low = 0
        high = len(nums) - 1
        k -= 1
        return self._findKthLargest(nums, k, low, high)
