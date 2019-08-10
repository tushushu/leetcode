# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-10 19:44:39
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def helper(self, root: TreeNode) -> list:
        if root is None:
            return []
        return self.helper(root.left) + [root.val] + self.helper(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        arr = self.helper(root)
        if len(arr) <= 1:
            return True
        ite = iter(arr)
        a = next(ite)
        for b in ite:
            if a >= b:
                return False
            a = b
        return True
