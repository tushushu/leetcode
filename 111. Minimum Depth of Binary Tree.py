# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-16 14:28:00
@Last Modified by:   tushushu
@Last Modified time: 2018-11-16 14:28:00
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        que = [(root, 1)]
        while que:
            node, depth = que.pop(0)
            if node.left or node.right:
                depth += 1
                if node.left:
                    que.append((node.left, depth))
                if node.right:
                    que.append((node.right, depth))
            else:
                return depth
