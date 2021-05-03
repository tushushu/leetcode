# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2021-05-03 22:54:02
@Last Modified by:   tushushu
@Last Modified time: 2021-05-03 22:54:02
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        len(s1) = m and len(s2) = n
        F(m, n) = (F(m - 1, n) AND S1[m - 1] == S3[m + n - 1])
        OR (F(m, n - 1) AND S2[n - 1] == S3[m + n - 1])
        """
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        F = [[False] * (n + 1) for _ in range(m + 1)]
        F[0][0] = True
        for i in range(m + 1):
            for j in range(n + 1):
                k = i + j - 1
                if j != 0:
                    F[i][j] = (F[i][j - 1] and s2[j - 1] == s3[k])
                if i != 0:
                    F[i][j] = F[i][j] or (F[i - 1][j] and s1[i - 1] == s3[k])
        return F[-1][-1]
