# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-26 11:48:28
@Last Modified by:   tushushu
@Last Modified time: 2018-10-26 11:48:28
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        que = [(root.left, root.right)]
        while que:
            left, right = que.pop(0)
            if left and right:
                if left.val != right.val:
                    return False
                else:
                    que.append((left.left, right.right))
                    que.append((left.right, right.left))
            elif left is None and right is None:
                pass
            else:
                return False
        return True
