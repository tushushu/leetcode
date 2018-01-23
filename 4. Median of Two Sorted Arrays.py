# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:29:54 2018

@author: Administrator
"""


class Solution:
    def findMedianSortedArrays1(self, nums1, nums2):
        a = len(nums1)
        b = len(nums2)
        k = 0
        n, m = divmod(a + b, 2)
        nums1.append(float('inf'))
        nums2.append(float('inf'))
        for i in range(n):
            if nums1[0] < nums2[0]:
                k = nums1.pop(0)
            else:
                k = nums2.pop(0)

        res = min(nums1[0], nums2[0])
        if m is 0:
            res = (k + res) / 2
        return res


    def findMedianSortedArrays(self, nums1, nums2):
        nums1.append(float('inf'))
        nums2.append(float('inf'))
        nums1.insert(0, -float('inf'))
        nums2.insert(0, -float('inf'))

        l1, l2 = len(nums1), len(nums2)
        n, odd = divmod(l1 + l2, 2)
        low = 0
        high = l1 - 1

        while(low <= high):
            i1 = (low + high) // 2
            i2 = n - i1 - 2
            if i2 < -1:
                high = i1 - 1
            elif i2 > l2 - 1:
                low = i1 + 1                
            elif i2 is not l2 - 1 and nums1[i1] > nums2[i2+1]:
                high = i1 - 1             
            elif i2 is not -1 and nums2[i2] > nums1[i1+1]:
                low = i1 + 1
            else:
                break
        if odd:
            res = min(nums1[i1+1], nums2[i2+1])
        else:
            res = (max(nums1[i1], nums2[i2]) + min(nums1[i1+1], nums2[i2+1])) / 2
        return res
