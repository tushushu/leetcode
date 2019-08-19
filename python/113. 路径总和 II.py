# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-19 10:43:28
"""
from typing import List
from copy import copy

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.target = None
        self.ret = None

    def helper(self, node: TreeNode, path: List[int]):
        if node is None:
            return
        path.append(node.val)
        if node.left is None and node.right is None:
            if sum(path) == self.target:
                self.ret.append(path)
            return
        self.helper(node.left, copy(path))
        self.helper(node.right, copy(path))

    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if root is None:
            return
        self.target = target
        self.ret = []
        self.helper(root, list())
        return self.ret
