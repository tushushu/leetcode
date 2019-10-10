# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-10-10 16:32:51
给定数组[1, 2...n-1, n]和数字m，0 < m < n，
求所有满足求和等于m的解。
举例：输入6, 7
返回：[[6], [1, 5], [2, 4], [1, 2, 3]]
"""


class FastSolution:
    def __init__(self):
        self.ret = None

    def helper(self, target, solution, total, start, end):
        if total == target:
            self.ret.append(solution)
            return
        if total > target or start > end:
            return
        # 不使用当前数字，提升搜索下限
        self.helper(target, solution, total, start+1, end)
        # 使用当前数字，提升下限同时降低上限
        total += start
        end = target - total  # 这一步优化是关键
        self.helper(target, solution + [start], total, start+1, end)

    def func(self, m, n):
        self.ret = []
        self.helper(m, [], 0, 1, min(m, n))
        return self.ret


"""
# 在Jupyter Notebook中运行
%%cython --cplus
from libcpp.vector cimport vector

cdef inline fmin(int x, int y):
    if x < y:
        return x
    return y

cdef class FasterSolution:
    cdef void helper(self, int target, vector[int] solution, int total, int start, int end, vector[vector[int]] &ret):
        if total == target:
            ret.push_back(solution)
            return
        if total > target or start > end:
            return
        # 不使用当前数字，提升搜索下限
        self.helper(target, solution, total, start+1, end, ret)
        # 使用当前数字，提升下限同时降低上限
        total += start
        end = target - total  # 这一步优化是关键
        solution.push_back(start)
        self.helper(target, solution, total, start+1, end, ret)

    cdef vector[vector[int]] _func(self, int m, int n):
        cdef vector[vector[int]] ret
        self.helper(m, [], 0, 1, fmin(m, n), ret)
        return ret
    
    def func(self, int m, int n):
        return self._func(m, n)
"""
