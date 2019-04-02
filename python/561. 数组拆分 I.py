# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-18 13:59:04
"""


class Solution:
    def partition(self, nums, low, high):
        i = low - 1
        for j in range(low, high):
            if nums[j] < nums[high]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                pass
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quick_sort(self, nums):
        low = 0
        high = len(nums) - 1
        que = [(low, high)]
        while que:
            low, high = que.pop(0)
            if low < high:
                mid = self.partition(nums, low, high)
                que.append((low, mid - 1))
                que.append((mid + 1, high))

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        self.quick_sort(nums)
        return sum(nums[::2])


if __name__ == "__main__":
    t = Solution()
    nums = [1, 2, 3, 2]
    t.quick_sort(nums)
    print(nums)
