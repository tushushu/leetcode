# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-04-22 22:54:18
@Last Modified by:   tushushu
@Last Modified time: 2021-04-22 22:54:18
"""
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        que: List[int] = []
        indexes: List[int] = []
        for i, x in enumerate(nums):
            if indexes and indexes[0] <= i - k:
                que.pop(0)
                indexes.pop(0)
            j = len(que) - 1
            while que:
                if que[j] <= x:
                    que.pop()
                    indexes.pop()
                    j -= 1
                else:
                    break
            que.append(x)
            indexes.append(i)
            if i >= k - 1:
                result.append(que[0])
        return result
