# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 21:46:06 2018

@author: Administrator
"""


class Solution:
    def partition(self, nums, low, high):
        i = low - 1
        j = low
        while j < high:
            if nums[j] <= nums[high]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def quick_sort(self, nums):
        low = 0
        high = len(nums) - 1
        if high < 1:
            return
        que = [(low, high)]
        while que:
            low, high = que.pop(0)
            i = self.partition(nums, low, high)
            if low < i - 1:
                que.append((low, i - 1))
            if i + 1 < high:
                que.append((i + 1, high))

    def combinationSum2(self, candidates, target):
        self.quick_sort(candidates)
        que = []
        last = None
        for i, num in enumerate(candidates):
            if num > target:
                break
            if i == 0:
                que.append(([num], num, i))
            else:
                if num != last:
                    que.append(([num], num, i))
            last = num
        n = len(candidates)
        print("candidates", candidates)
        ret = []
        while que:
            nums, tot, i = que.pop(0)
            print(nums, tot, i)
            if tot == target:
                ret.append(nums)
                print(ret)
            elif tot < target:
                if i + 1 < n:
                    nums.append(candidates[i + 1])
                    que.append((nums, tot + candidates[i + 1], i + 1))
            else:
                pass
        return ret


if __name__ == "__main__":
    test = Solution()
    test.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
