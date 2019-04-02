# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-16 15:30:46
"""


class Solution:
    def bin_search_range(self, arr, target, t):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < target - t:
                low = mid + 1
            elif arr[mid] > target + t:
                high = mid - 1
            else:
                return True
        return False

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        unique = set()
        for i, num in enumerate(nums):
            if i > k:
                unique.remove(nums[i - k - 1])
            arr = sorted(unique)
            if self.bin_search_range(arr, num, t):
                return True
            else:
                unique.add(num)
        return False


if __name__ == "__main__":
    t = Solution()
    t.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)
