# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-16 16:09:05
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

    def helper(self, node: TreeNode, depth: int, index: int):
        if node is None:
            return
        if node.left is None and node.right is None:
            if self.ret.get(depth):
                if index < self.ret.get(depth)[0]:
                    self.ret[depth] = (index, node.val)
            else:
                self.ret[depth] = (index, node.val)
        self.helper(node.left, depth + 1, index * 2)
        self.helper(node.right, depth + 1, index * 2 + 1)

    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root is None:
            return None
        self.ret = dict()
        self.helper(root, 0, 0)
        return self.ret[max(self.ret)][1]
