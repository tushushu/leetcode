# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:40:50 2018

@author: Administrator
"""
from copy import copy


class Solution:
    def helper(self, mat, idx):
        if idx+1 == len(mat[0]):
            return mat
        res = []
        for nums in mat:
            for i in range(idx, len(nums)):
                tmp = copy(nums)
                tmp.insert(idx, tmp.pop(i))
                res.append(tmp)
        return self.helper(res, idx+1)

    def permute(self, nums):
        if nums == []:
            return [[]]
        return self.helper([nums], 0)
