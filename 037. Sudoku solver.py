#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 12:21:44 2018

@author: Tuzi
"""
from itertools import product, combinations, chain
from copy import deepcopy

class Solution:
    def _fill_board(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    board[i][j] = '123456789'

    def _col_eliminate(self, board, solved, x, j):
        for i in range(9):
            y = board[i][j]
            if len(y) > 1:
                board[i][j] = y.replace(x, '')
                if len(board[i][j]) == 1:
                    solved.append([i, j])


    def _row_eliminate(self, board, solved, x, i):
        for j, y in enumerate(board[i]):
            if len(y) > 1:
                board[i][j] = y.replace(x, '')
                if len(board[i][j]) == 1:
                    solved.append([i, j])

    def _sub_board_eliminate(self, board, solved, x, i, j):
        h = i // 3 * 3
        v = j // 3 * 3
        for ii, jj in product(range(h, h+3), range(v, v+3)):
            y = board[ii][jj]
            if len(y) > 1:
                board[ii][jj] = y.replace(x, '')
                if len(board[ii][jj]) == 1:
                    solved.append([i, j])

    def _board_eliminate(self, board):
        solved = [[i, j] for i, j in product(range(9), range(9)) if len(board[i][j]) == 1]
        while solved:
            i, j = solved.pop()
            x = board[i][j]
            self._col_eliminate(board, solved, x, j)
            self._row_eliminate(board, solved, x, i)
            self._sub_board_eliminate(board, solved, x, i, j)
    
    def _is_valid(self, board):
        for row in board:
            if any(x1 == x2 for x1, x2 in combinations(row, 2) if len(x1) == 1 and len(x2) == 1):
                return False
        for col in map(list, zip(*board)):
            if any(x1 == x2 for x1, x2 in combinations(col, 2) if len(x1) == 1 and len(x2) == 1):
                return False
        for i, j in product(range(0, 9, 3), range(0, 9, 3)):
            if any(x1 == x2 for x1, x2 in combinations(chain(*map(lambda x: x[j:j+3], board[i:i+3])),2) if len(x1) == 1 and len(x2) == 1):
                return False
        return True
    
    def _dfs_search(self, board):
        cnt = 0
        for k, x in enumerate(chain(*board)):
            if len(x) > 1:
                break
            else:
                cnt += 1

        if cnt == 81:
            return board

        i = k // 9
        j = k % 9
        for digit in x:
            board[i][j] = digit
            if self._is_valid(board):
                res = self._dfs_search(deepcopy(board))
                if res is not None:
                    return res

    def _bfs_search(self, board):
        unsolved = [[k // 9, k % 9] for k, x in enumerate(chain(*board)) if len(x) > 1]
        que = [deepcopy(board)]
        while unsolved:
            i, j = unsolved.pop(0)
            L = len(que)
            for _ in range(L):
                item = que.pop(0)
                x = item[i][j]
                for digit in x:
                    item[i][j] = digit
                    if self._is_valid(item):
                        que.append(deepcopy(item))
        return que[0]

    def solveSudoku(self, board):
        self._fill_board(board)
        self._board_eliminate(board)
        res = self._dfs_search(board)
#        res = self._bfs_search(board)
        for i in range(9):
            for j in range(9):
                board[i][j] = res[i][j]



    def test1(self):
        s = '53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79'
        assert len(s) == 81, "length of board must be 81"
        board = []
        row = []
        for i, c in enumerate(s):
            row.append(c)
            if i % 9 == 8:
                board.append(row)
                row = []
        self.solveSudoku(board)
        for row in board:
            print(row)

    def test2(self):
        board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
        self.solveSudoku(board)
        for row in board:
            print(row)
            
    def test3(self):
        board = [[".","2","6","5",".",".",".","9","."],["5",".",".",".","7","9",".",".","4"],["3",".",".",".","1",".",".",".","."],["6",".",".",".",".",".","8",".","7"],[".","7","5",".","2",".",".","1","."],[".","1",".",".",".",".","4",".","."],[".",".",".","3",".","8","9",".","2"],["7",".",".",".","6",".",".","4","."],[".","3",".","2",".",".","1",".","."]]
        self.solveSudoku(board)
        for row in board:
            print(row)

t = Solution()
t.test1()
t.test2()
t.test3()
