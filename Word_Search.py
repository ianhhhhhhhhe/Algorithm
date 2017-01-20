class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.checker(board, word, i, j):
                    return True
        return False

    def checker(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = " "
            if i > 0 and self.checker(board, word[1:], i-1, j):
                return True
            if i < len(board)-1 and self.checker(board, word[1:], i+1, j):
                return True
            if j > 0 and self.checker(board, word[1:], i, j-1):
                return True
            if j < len(board[0])-1 and self.checker(board, word[1:], i, j+1):
                return True
            board[i][j] = word[0]
            return False
        else:
            return False
