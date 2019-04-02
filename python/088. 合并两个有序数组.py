# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-12 14:09:01
"""


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        for k in range(m + n - 1, -1, -1):
            if i == -1:
                nums1[k] = nums2[j]
                j -= 1
                continue
            if j == -1:
                nums1[k] = nums1[i]
                i -= 1
                continue
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1


if __name__ == "__main__":
    t = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    t.merge(nums1, m, nums2, n)
