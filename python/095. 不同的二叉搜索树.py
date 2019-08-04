# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-02-12 14:09:01
"""
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "val %s" % self.val


class Solution:
    def helper(self, start, end):
        if start > end:
            yield None
        for val in range(start, end + 1):
            for left in self.helper(start, val - 1):
                for right in self.helper(val + 1, end):
                    root = TreeNode(val)
                    root.left = left
                    root.right = right
                    yield root

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return list(self.helper(1, n))
