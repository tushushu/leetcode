# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 15:44:53 2018

@author: Administrator
"""


class Solution:
    def __init__(self):
        self.dic = {1: 'I', 10: 'X', 100: 'C', 1000: 'M'
                    , 5: 'V', 50: 'L', 500: 'D'
                    , 4: 'IV', 40: 'XL', 400: 'CD'
                    , 9: 'IX', 90: 'XC', 900: 'CM'}
        self.nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000, 4000]

    def binSearch(self, num):
        left = 0
        right = len(self.nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if num < self.nums[mid]:
                right = mid - 1
            elif num >= self.nums[mid + 1]:
                left = mid + 1
            else:
                break
        return self.nums[mid]

    def intToRoman(self, num):
        res = ''
        while num != 0:
            v = self.binSearch(num)
            num -= v
            res += self.dic[v]
        return res
