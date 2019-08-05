# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-05 21:51:18
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, root: TreeNode) -> set:
        if root is None:
            return {0}
        left = {root.val + x for x in self.helper(root.left)}
        if root.left is not None and root.right is None:
            return left
        right = {root.val + x for x in self.helper(root.right)}
        if root.right is not None and root.left is None:
            return right
        return left | right

    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if root is None:
            return False
        return target in self.helper(root)
