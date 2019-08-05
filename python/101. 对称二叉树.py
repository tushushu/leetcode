# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-05 20:34:23
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.order = []
        self.reversed = []

    def pre_order(self, root: TreeNode):
        if root is None:
            self.order.append(None)
        else:
            self.order.append(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def reverse_order(self, root: TreeNode):
        if root is None:
            self.reversed.append(None)
        else:
            self.reversed.append(root.val)
            self.reverse_order(root.right)
            self.reverse_order(root.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        self.pre_order(root)
        self.reverse_order(root)
        return self.order == self.reversed
