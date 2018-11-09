# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-09 10:51:31
@Last Modified by:   tushushu
@Last Modified time: 2018-11-09 10:51:31
"""


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        p = 0
        q = 1
        n = len(A) - 1
        while 1:
            while A[p] % 2 == 0:
                p += 2
                if p > n - 1:
                    return A
            while q < n and A[q] % 2 == 1:
                q += 2
                if q > n:
                    return A
            A[p], A[q] = A[q], A[p]
