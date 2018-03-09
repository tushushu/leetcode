# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 19:29:14 2018

@author: Administrator
"""


class Solution:
    def twoSum(self, nums, target):
        res = []
        l, r = 0, len(nums)-1
        if (target >= 0 and (target < nums[l] * 2 or target > nums[r] * 2)) or \
           (target < 0 and (target < nums[r] * 2 or target > nums[l] * 2)):
            return res
        while l < r:
            if nums[l] + nums[r] == target:
                res.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while r > l and nums[r] == nums[r + 1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                if target >= 0:
                    l += 1
                else:
                    r -= 1
            else:
                if target >= 0:
                    r -= 1
                else:
                    l += 1
        return res

    def nSum(self, nums, target, n):
        results = []
        if n == 2:
            return self.twoSum(nums, target)
        for i in range(len(nums) - n + 1):
            if (target >= 0 and (target < nums[i] * n or target > nums[-1] * n)) or \
               (target < 0 and (target < nums[-1] * n or target > nums[i] * n)):
                break
            if target >= 0:
                if nums[i] > target:
                    break
            else:
                if nums[i] < target:
                    break
                pass
            if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                results.extend([[nums[i]] + x for x in self.nSum(nums[i+1:], target-nums[i], n-1)])
        return results

    def fourSum(self, nums, target):
        reverse = (target < 0)
        nums.sort(reverse=reverse)
        return self.nSum(nums, target, 4)

test = Solution()
nums = [-1, 0, 1, 2, -1, -4]
target = -1
test.fourSum(nums, target)
