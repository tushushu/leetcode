# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-29 12:00:09
"""


class Solution:
    def helper(self, a, b):
        return (b[0] - a[0]) * 60 + (b[1] - a[1])

    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        arr = [list(map(int, x.split(":"))) for x in timePoints]
        arr.sort()
        for i in range(len(arr)):
            arr.append([arr[i][0] + 24, arr[i][1]])

        return min(map(lambda x: self.helper(arr[x], arr[x + 1]),
                       range(len(arr) - 1)))


if __name__ == "__main__":
    t = Solution()
    t.findMinDifference(["23:59", "00:00"])
