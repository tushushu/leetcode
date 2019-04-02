# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 17:23:06 2018

@author: Administrator
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            m = len(matrix[0]) - 1
            for i in range(m//2 + 1):
                for j in range(i, m-i):
                    matrix[i][j], matrix[j][m-i], matrix[m-i][m-j], matrix[m-j][i] =\
                        matrix[m-j][i], matrix[i][j], matrix[j][m -
                                                                i], matrix[m-i][m-j]
        else:
            return None
