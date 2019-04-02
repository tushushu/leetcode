# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-26 12:05:28
@Last Modified by:   tushushu
@Last Modified time: 2018-10-26 12:05:28
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ret = []
        que = [(root, 1)]
        while que:
            node, depth = que.pop(0)
            if depth == len(ret):
                ret[depth - 1].append(node.val)
            else:
                ret.append([node.val])
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        return ret[::-1]