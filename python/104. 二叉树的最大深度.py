# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-05 20:54:06
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        left += 1
        right += 1
        return max(left, right)
