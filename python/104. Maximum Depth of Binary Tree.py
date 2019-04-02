# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-26 12:01:20
@Last Modified by:   tushushu
@Last Modified time: 2018-10-26 12:01:20
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        que = [(root, 1)]
        while que:
            node, depth = que.pop(0)
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        return depth
