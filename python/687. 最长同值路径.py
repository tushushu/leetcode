# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-01-28 13:56:02
"""
from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = 0

    def helper(self, root: TreeNode):
        if root is None:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        left = left + 1 if root.left is not None and root.left.val == root.val else 0
        right = right + 1 if root.right is not None and root.right.val == root.val else 0

        self.ret = max(self.ret, left + right)
        return max(left, right)

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.helper(root)
        return self.ret
