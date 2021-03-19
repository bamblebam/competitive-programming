class Solution:
    def helper(self, board, word, i, j, count):
        if count == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[count]:
            return False
        temp = board[i][j]
        board[i][j] = None
        found = self.helper(board, word, i-1, j, count+1) or self.helper(board, word, i+1, j, count +
                                                                         1) or self.helper(board, word, i, j-1, count+1) or self.helper(board, word, i, j+1, count+1)
        board[i][j] = temp
        return found

    def exist(self, board, word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.helper(board, word, i, j, 0):
                    return True
        return False


sol = Solution()
print(sol.exist(board=[["A", "B", "C", "E"], [
      "S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEETFD"))
