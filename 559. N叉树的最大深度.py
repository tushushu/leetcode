# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-10 19:36:04
"""

# Definition for a Node.


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        if root is None:
            return 0
        if root.children:
            return max([self.maxDepth(child) + 1 for child in root.children])
        return 1
