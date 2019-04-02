# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-10-29 14:11:53
@Last Modified by:   tushushu
@Last Modified time: 2018-10-29 14:11:53
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        if t1 is None and t2 is not None:
            return t2
        if t1 is not None and t2 is None:
            return t1
        que = [(t1, t2)]
        while que:
            tree1, tree2 = que.pop(0)
            tree1.val += tree2.val
            if tree1.left or tree2.left:
                if tree2.left is None:
                    tree2.left = TreeNode(0)
                elif tree1.left is None:
                    tree1.left = TreeNode(0)
                que.append((tree1.left, tree2.left))

            if tree1.right or tree2.right:
                if tree2.right is None:
                    tree2.right = TreeNode(0)
                elif tree1.right is None:
                    tree1.right = TreeNode(0)
                que.append((tree1.right, tree2.right))

        return t1
