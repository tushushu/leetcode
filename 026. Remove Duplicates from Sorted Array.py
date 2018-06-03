<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:14:06 2018

@author: Administrator
"""


class Solution:
    def removeDuplicates(self, nums):
        res = 0
        last = float('-inf')
        i = 0
        while i < len(nums):
            num = nums[i]
            if num != last:
                res += 1
                i += 1
                last = num
            else:
                nums.pop(i)
        return res
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:14:06 2018

@author: Administrator
"""


class Solution:
    def removeDuplicates(self, nums):
        res = 0
        last = float('-inf')
        i = 0
        while i < len(nums):
            num = nums[i]
            if num != last:
                res += 1
                i += 1
                last = num
            else:
                nums.pop(i)
        return res
>>>>>>> c9978dc9fcf21f5c72e7576e1b249d22946c4f1e
