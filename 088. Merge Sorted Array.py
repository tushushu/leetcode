# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-25 14:38:13
@Last Modified by:   tushushu
@Last Modified time: 2018-10-25 14:38:13
"""


class Solution:
    def helper(self, nums, k):
        if k == -1:
            return -float("inf")
        else:
            return nums[k]

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p = m - 1
        q = n - 1
        i = m + n - 1
        while q >= 0:
            a = self.helper(nums1, p)
            b = self.helper(nums2, q)
            if a > b:
                nums1[i] = nums1[p]
                p -= 1
            else:
                nums1[i] = nums2[q]
                q -= 1
            i -= 1


def main():
    t = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    t.merge(nums1, m, nums2, n)
    print(nums1)

if __name__ == '__main__':
    main()
