<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:23:22 2018

@author: Administrator
"""


class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        subs = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char is '.':
                    continue
                k = (i // 3) + 3 * (j // 3)
                if char in rows[i] or char in columns[j] or char in subs[k]:
                    return False
                else:
                    rows[i].add(char)
                    columns[j].add(char)
                    subs[k].add(char)
        return True
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:23:22 2018

@author: Administrator
"""


class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        subs = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char is '.':
                    continue
                k = (i // 3) + 3 * (j // 3)
                if char in rows[i] or char in columns[j] or char in subs[k]:
                    return False
                else:
                    rows[i].add(char)
                    columns[j].add(char)
                    subs[k].add(char)
        return True
>>>>>>> c9978dc9fcf21f5c72e7576e1b249d22946c4f1e
