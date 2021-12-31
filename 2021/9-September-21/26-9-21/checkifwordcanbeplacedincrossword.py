class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        n = len(word)

        # row check
        for i in range(rows):
            if cols-board[i].count('#') < n:
                continue
            # left to right
            k = 0
            for j in range(cols):
                if k >= n:
                    k = 0
                if board[i][j] == " ":
                    k += 1
                elif board[i][j] != " " and board[i][j] != "#":
                    if word[k] == board[i][j]:
                        k += 1
                    else:
                        k = 0
                else:
                    k = 0
                if k == n:
                    if 0 <= j+1 < cols and board[i][j+1] == '#' and 0 <= j-n < cols and board[i][j-n] == '#':
                        return True
                    elif not 0 <= j+1 < cols and not 0 <= j-n < cols:
                        return True
                    elif not 0 <= j+1 < cols and (0 <= j-n < cols and board[i][j-n] == '#'):
                        return True
                    elif not 0 <= j-n < cols and (0 <= j+1 < cols and board[i][j+1] == '#'):
                        return True
            # right to left
            k = 0
            row = list(reversed(board[i]))
            for j in range(cols):
                if k >= n:
                    k = 0
                if row[j] == " ":
                    k += 1
                elif row != " " and row[j] != "#":
                    if word[k] == row[j]:
                        k += 1
                    else:
                        k = 0
                else:
                    k = 0
                # if k==n:
                #     return True
                if k == n:
                    if 0 <= j+1 < cols and row[j+1] == '#' and 0 <= j-n < cols and row[j-n] == '#':
                        return True
                    elif not 0 <= j+1 < cols and not 0 <= j-n < cols:
                        return True
                    elif not 0 <= j+1 < cols and (0 <= j-n < cols and row[j-n] == '#'):
                        return True
                    elif not 0 <= j-n < cols and (0 <= j+1 < cols and row[j+1] == '#'):
                        return True

        #transpose_matrix and reinitialize
        board = [list(row) for row in zip(*board)]
        rows = len(board)
        cols = len(board[0])
        # col check
        for i in range(rows):
            if cols-board[i].count('#') < n:
                continue
            # left to right
            k = 0
            for j in range(cols):
                if k >= n:
                    k = 0
                if board[i][j] == " ":
                    k += 1
                elif board[i][j] != " " and board[i][j] != "#":
                    if word[k] == board[i][j]:
                        k += 1
                    else:
                        k = 0
                else:
                    k = 0
                if k == n:
                    if 0 <= j+1 < cols and board[i][j+1] == '#' and 0 <= j-n < cols and board[i][j-n] == '#':
                        return True
                    elif not 0 <= j+1 < cols and not 0 <= j-n < cols:
                        return True
                    elif not 0 <= j+1 < cols and (0 <= j-n < cols and board[i][j-n] == '#'):
                        return True
                    elif not 0 <= j-n < cols and (0 <= j+1 < cols and board[i][j+1] == '#'):
                        return True
            # right to left
            k = 0
            row = list(reversed(board[i]))
            for j in range(cols):
                if k >= n:
                    k = 0
                if row[j] == " ":
                    k += 1
                elif row != " " and row[j] != "#":
                    if word[k] == row[j]:
                        k += 1
                    else:
                        k = 0
                else:
                    k = 0
                # if k==n:
                #     return True
                if k == n:
                    if 0 <= j+1 < cols and row[j+1] == '#' and 0 <= j-n < cols and row[j-n] == '#':
                        return True
                    elif not 0 <= j+1 < cols and not 0 <= j-n < cols:
                        return True
                    elif not 0 <= j+1 < cols and (0 <= j-n < cols and row[j-n] == '#'):
                        return True
                    elif not 0 <= j-n < cols and (0 <= j+1 < cols and row[j+1] == '#'):
                        return True

        return False
