class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[0]*3 for _ in range(3)]
        moves_count = 0

        def check():
            # for row
            for row in grid:
                if 'X' in row and len(set(row)) == 1:
                    return 'X'
                if 'O' in row and len(set(row)) == 1:
                    return 'O'

            # for col
            for j in range(3):
                col = set()
                for i in range(3):
                    col.add(grid[i][j])
                if 'X' in col and len(col) == 1:
                    return 'X'
                if 'O' in col and len(col) == 1:
                    return 'O'

            # for diagonal
            for i, token in enumerate(['X', 'O']):
                if any([grid[0][0] == token, grid[1][1] == token, grid[2][2] == token]) and (grid[0][0] == grid[1][1] == grid[2][2]):
                    return token
                if any([grid[0][2] == token, grid[1][1] == token, grid[2][0] == token]) and (grid[0][2] == grid[1][1] == grid[2][0]):
                    return token

            # for none
            return None

        # for moves
        for i, [x, y] in enumerate(moves):
            if i % 2:
                token = 'O'
            else:
                token = 'X'
            grid[x][y] = token
            moves_count += 1
            if moves_count >= 5:
                t = check()
                if t == 'X':
                    return 'A'
                elif t == 'O':
                    return 'B'

        # after moves are done
        if moves_count == 9:
            return 'Draw'
        return 'Pending'
