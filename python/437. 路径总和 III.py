# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-09-08 11:07:01
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = 0

    def helper(self, node, target, tot):
        if node is None:
            return
        tot += node.val
        if tot == target:
            self.ret += 1
        self.helper(node.left, target, tot)
        self.helper(node.right, target, tot)

    def pathSum(self, root: TreeNode, target: int) -> int:
        if root is None:
            return 0
        que = [root]
        while que:
            node = que.pop(0)
            self.helper(node, target, 0)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return self.ret
