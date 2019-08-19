# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2019-08-18 13:46:55
"""

# Definition for a Node.


class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if root is None:
            return
        if root.left:
            if root.right:
                root.left.next = root.right
                child = root.right
            else:
                child = root.left
        else:
            child = root.right
        parent = root.next
        while child and parent:
            if parent.left:
                child.next = parent.left
                break
            if parent.right:
                child.next = parent.right
                break
            parent = parent.next
        # 这里注意一定要先构建右子树，再构建左子树，因为寻找父节点的兄弟节点
        # 是从左到右遍历的，如果右子树未构建好就遍历，则会出错
        self.connect(root.right)
        self.connect(root.left)
        return root
