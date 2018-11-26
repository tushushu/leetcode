# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-26 18:40:00
@Last Modified by:   tushushu
@Last Modified time: 2018-11-26 18:40:00
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                if i - dic[num] <= k:
                    return True
                else:
                    dic[num] = i
            else:
                dic[num] = i
        return False
