# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-16 14:36:19
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = None

    def helper(self, node: TreeNode, num: int):
        if node is None:
            return
        num = num * 10 + node.val
        if node.left is None and node.right is None:
            self.ret += num
            return
        self.helper(node.left, num)
        self.helper(node.right, num)

    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.ret = 0
        self.helper(root, 0)
        return self.ret
