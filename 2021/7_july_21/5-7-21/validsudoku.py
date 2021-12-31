class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            rowlist = list()
            rowset = set()
            row = board[i]
            for j in row:
                if j != ".":
                    rowlist.append(j)
                    rowset.add(j)
            if len(rowlist) != len(rowset):
                return False

        for i in range(9):
            collist = list()
            colset = set()
            for j in range(9):
                if board[j][i] != ".":
                    collist.append(board[j][i])
                    colset.add(board[j][i])
            if len(collist) != len(colset):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                boxlist = list()
                boxset = set()
                for l in range(3):
                    for m in range(3):
                        if board[i+l][j+m] != ".":
                            boxlist.append(board[i+l][j+m])
                            boxset.add(board[i+l][j+m])
                if len(boxlist) != len(boxset):
                    return False

        return True
