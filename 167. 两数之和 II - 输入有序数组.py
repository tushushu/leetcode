# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-13 13:40:41
"""


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for i, num in enumerate(numbers):
            if num in dic:
                return dic[num] + 1, i + 1
            else:
                dic[target - num] = i
