# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-19 17:00:45
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums) - 1
        if target <= nums[0]:
            return 0
        if target > nums[n]:
            return n + 1
        low = 0
        high = n
        while 1:
            mid = (low + high) // 2
            if nums[mid - 1] < target <= nums[mid]:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1


if __name__ == "__main__":
    t = Solution()
    nums = [1, 3, 5, 6]
    target = 2
    print(t.searchInsert(nums, target))
