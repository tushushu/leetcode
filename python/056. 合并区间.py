# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-04-03 16:47:41
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def helper(self, arr, x):
        if arr == []:
            arr.append(x)
            return

        y = arr[-1]
        if x.start > y.end:
            arr.append(x)
        else:
            y.start = min(x.start, y.start)
            y.end = max(x.end, y.end)

    def merge(self, intervals):
        que = [[x] for x in intervals]
        while len(que) > 1:
            left = que.pop(0)
            right = que.pop(1)
            arr = []
            while left and right:
                if left[0].start > right[0].start:
                    self.helper(arr, left.pop(0))
                else:
                    self.helper(arr, right.pop(0))
            else:
                pass
