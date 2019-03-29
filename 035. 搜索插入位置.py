# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-03-29 15:17:09
"""


class Solution:
    def searchInsert(self, nums, target):
        n = len(nums) - 1
        if target <= nums[0]:
            return 0
        if target > nums[n]:
            return n + 1
        low = 0
        high = n
        while 1:
            mid = (low + high) // 2
            if nums[mid] > target:
                if nums[mid - 1] < target:
                    return mid
                elif nums[mid - 1] == target:
                    return mid - 1
                else:
                    high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid


if __name__ == "__main__":
    t = Solution()
    print(t.searchInsert([1, 3], 2))
