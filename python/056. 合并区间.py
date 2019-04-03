# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-04-03 16:47:41
"""
# Definition for an interval.


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def helper(self, arr, x):
        # s = [[y.start, y.end] for y in arr]
        # print('start', s, [x.start, x.end])
        if arr == []:
            arr.append(x)
            return

        if x.start > arr[-1].end:
            arr.append(x)
        else:
            arr[-1].end = x.end
        # s = [[y.start, y.end] for y in arr]
        # print('end', s, [x.start, x.end])

    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        que = [[x] for x in intervals]
        while len(que) > 1:
            # s = [[[y.start, y.end] for y in x] for x in que]
            # print("start", s)
            left = que.pop(0)
            right = que.pop(0)
            arr = []
            while left and right:
                if left[0].start < right[0].start:
                    self.helper(arr, left.pop(0))
                else:
                    self.helper(arr, right.pop(0))
            other = left if left else right
            while other:
                self.helper(arr, other.pop(0))
            que.append(arr)
            # s = [[[y.start, y.end] for y in x] for x in que]
            # print("end", s)
        return que[0]


if __name__ == "__main__":
    intervals = []
    intervals = [Interval(x[0], x[1]) for x in intervals]
    t = Solution()
    print("ret\n", t.merge(intervals))
