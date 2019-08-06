# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-06 19:59:07
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
        self.ret = []

    def helper(self, root: TreeNode, path: str):
        if root is None:
            return
        if path == "":
            path = str(root.val)
        else:
            path += "->%s" % root.val
        if root.left is None and root.right is None:
            self.ret.append(path)
        self.helper(root.left, path)
        self.helper(root.right, path)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.helper(root, "")
        return self.ret
