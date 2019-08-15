# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-15 14:21:46
"""
from typing import List


class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = None

    def helper(self, node: TreeNode, depth: int):
        if node is None:
            return
        if depth in self.ret:
            self.ret[depth] = max(node.val, self.ret[depth])
        else:
            self.ret[depth] = node.val
        self.helper(node.left, depth + 1)
        self.helper(node.right, depth + 1)

    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self.ret = dict()
        self.helper(root, 0)
        return [self.ret[i] for i in range(len(self.ret))]
