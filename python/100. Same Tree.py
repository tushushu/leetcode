# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        que = [(p, q)]
        while que:
            p, q = que.pop(0)
            if p is not None and q is not None:
                if p.val != q.val:
                    return False
                else:
                    que.append((p.left, q.left))
                    que.append((p.right, q.right))
            elif p is None and q is None:
                pass
            else:
                return False
        return True
