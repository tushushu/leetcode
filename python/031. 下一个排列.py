# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-03-12 17:06:26
"""


class Solution:
    def nextPermutation(self, nums: list) -> None:
        n = len(nums)
        # 寻找逆序对
        high = n - 1
        i = high - 1
        while nums[i] >= nums[i + 1] and i != -1:
            i -= 1
        # 将逆序对右侧的数组倒序排列
        low = i + 1
        while low <= high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
        # 如果不存在逆序对则返回
        if i == -1:
            return None
        else:
            target = nums[i]
        # 二分查找逆序对右侧大于target的最小数
        low = i + 1
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            left = -float("inf") if mid == low else nums[mid - 1]
            right = nums[mid]
            if target >= left and target < right:
                break
            elif target < left:
                high = mid - 1
            else:
                low = mid + 1
        # 交换，形成新的排列
        nums[i], nums[mid] = nums[mid], nums[i]


if __name__ == "__main__":
    nums = [2, 2, 7, 5, 4, 3, 2, 2, 1]
    t = Solution()
    t.nextPermutation(nums)
