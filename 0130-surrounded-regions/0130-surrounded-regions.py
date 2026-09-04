class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        r=len(board)
        c=len(board[0])

        mark=[[0 for _ in range(c)] for _ in range(r)]
        def dfs(i,j,mark,board):
            if mark[i][j]==1:
                return
            mark[i][j]=1
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_i,new_j=i+dx,j+dy
                if new_i<0 or new_i>=len(board) or new_j<0 or new_j>=len(board[0]) or board[new_i][new_j]=="X" or mark[new_i][new_j]==1:
                    continue
                dfs(new_i,new_j,mark,board)

        for j in range(c):
            if board[0][j]=="O":
                dfs(0,j,mark,board)
        
    # 2. Right Column (Top to Bottom) - Start at row 1 to avoid double-counting the top-right corner
        for i in range(1, r):
            if board[i][c-1]=="O":
                dfs(i,c-1,mark,board)
        
        
    # 3. Bottom Row (Right to Left) - Check if r > 1 to avoid duplicating the top row in a 1D array
        if r > 1:
            for j in range(c - 2, -1, -1):
                if board[r-1][j]=="O":
                    dfs(r-1,j,mark,board)
            
            
    # 4. Left Column (Bottom to Top) - Check if c > 1 to avoid duplicating the right column
        if c > 1:
            for i in range(r - 2, 0, -1):
                if board[i][0]=="O":
                    dfs(i,0,mark,board)
        
        
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O" and mark[i][j] == 0:
                    board[i][j]="X"
        return board
            

        