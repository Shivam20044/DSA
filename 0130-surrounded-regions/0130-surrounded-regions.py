class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        r = len(board)
        c = len(board[0])

        def dfs(i, j):
            # Base case: stop if out of bounds or if the cell is not 'O'
            if i < 0 or i >= r or j < 0 or j >= c or board[i][j] != "O":
                return
            
            # Temporarily mark the safe 'O' as 'T'
            board[i][j] = "T"
            
            # Flood fill in all 4 directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # 1. Check Top and Bottom rows
        for j in range(c):
            if board[0][j] == "O": dfs(0, j)
            if board[r-1][j] == "O": dfs(r-1, j)
                
        # 2. Check Left and Right columns (skipping corners to avoid redundancy)
        for i in range(1, r - 1):
            if board[i][0] == "O": dfs(i, 0)
            if board[i][c-1] == "O": dfs(i, c-1)

        # 3. Final Pass: Flip remaining 'O's to 'X', and restore 'T's back to 'O'
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"