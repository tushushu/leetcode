# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-11 10:28:48
"""
from itertools import zip_longest


class Solution:
    def helper(self, version):
        i = 0
        for j, c in enumerate(version):
            if c is ".":
                yield int(version[i:j])
                i = j + 1
        yield int(version[i:])

    def compareVersion(self, version1, version2):
        nums1 = self.helper(version1)
        nums2 = self.helper(version2)
        for a, b in zip_longest(nums1, nums2, fillvalue=0):
            if a != b:
                return [-1, 1][a > b]
        return 0


if __name__ == "__main__":
    t = Solution()
    print(t.compareVersion("1", "1.1"))
