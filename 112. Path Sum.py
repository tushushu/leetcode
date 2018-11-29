# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-11-29 11:56:51
@Last Modified by:   tushushu
@Last Modified time: 2018-11-29 11:56:51
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        ret = set()
        que = [(root, root.val)]
        while que:
            node, tot = que.pop(0)
            if node.left:
                que.append((node.left, tot + node.left.val))
            if node.right:
                que.append((node.right, tot + node.right.val))
            if node.left is None and node.right is None:
                ret.add(tot)
            if target in ret:
                return True
        return False
