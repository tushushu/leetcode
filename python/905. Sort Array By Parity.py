# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-30 10:58:02
@Last Modified by:   tushushu
@Last Modified time: 2018-10-30 10:58:02
"""


class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = -1
        for j in range(len(A)):
            if A[j] % 2 == 0:
                i += 1
                A[i], A[j] = A[j], A[i]
        return A
