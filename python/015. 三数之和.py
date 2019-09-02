# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-02 11:42:11
"""
from typing import List
from collections import Counter
from itertools import chain


class Solution:
    def two_sum(self, target, arr):
        ret = set()
        d = dict()
        for x in arr:
            if x in d:
                ret.add(",".join(map(str, sorted([-target, x, d[x]]))))
            else:
                d[target - x] = x
        return ret

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        arr = list(chain(*[[k] * min(3, v) for k, v in cnt.items()]))
        unique = set()
        for i, x in enumerate(arr):
            unique |= self.two_sum(-x, arr[i + 1:])
        ret = [list(map(int, x.split(","))) for x in unique]
        return ret
