from collections import defaultdict


class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def helper(board, empty, rows, cols, boxes):
            if not empty:
                return True
            r, c = empty[-1]
            for k in set('123456789')-(rows[r] | cols[c] | boxes[3*(r//3)+c//3]):
                board[r][c] = k
                for dic in [rows[r], cols[c], boxes[3*(r//3)+c//3]]:
                    dic.add(k)
                if helper(board, empty[:-1], rows, cols, boxes):
                    return True
                board[r][c] = '.'
                for dic in [rows[r], cols[c], boxes[3*(r//3)+c//3]]:
                    dic.remove(k)
            return False

        empty = list()
        rows, cols, boxes = defaultdict(
            set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    for dic in [rows[i], cols[j], boxes[3*(i//3)+j//3]]:
                        dic.add(board[i][j])

        helper(board, empty, rows, cols, boxes)
