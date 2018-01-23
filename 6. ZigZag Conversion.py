# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:59:59 2018

@author: Administrator
"""


class Solution:
    def next(self, i, numRows, direction):
        if numRows == 1:
            pass
        else:
            i = i + direction
            if i == -1 or i == numRows:
                direction = -direction
                i += direction * 2
        return i, direction

    def convert(self, s, numRows):
        res = [[] for _ in range(numRows)]
        i = 0
        direction = 1
        for char in s:
            res[i].append(char)
            i, direction = self.next(i, numRows, direction)
        return ''.join([''.join(x) for x in res])

    def convert1(self, s, numRows):
        step = (numRows == 1) - 1  # 0 or -1
        rows, idx = [''] * numRows, 0
        for c in s:
            rows[idx] += c
            if idx == 0 or idx == numRows-1:
                step = -step  # change direction
            idx += step
        return ''.join(rows)
