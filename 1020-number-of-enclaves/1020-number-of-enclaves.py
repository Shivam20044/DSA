class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        cols=len(grid[0])
        count=0
        queue=deque()
        visited=[[0 for _ in range(cols)] for _ in range(rows)]
        for j in range(cols):
            if grid[0][j] == 1:
                queue.append((0,j))

            if grid[rows-1][j] == 1:
                queue.append((rows-1,j))

                
        for i in range(1, rows - 1):
            if grid[i][0] == 1:
                queue.append((i,0))
            if grid[i][cols-1] == 1:
                queue.append((i,cols-1))
        
        while queue:
            i,j=queue.popleft()
            if visited[i][j]==1:
                continue
            visited[i][j]=1
            for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_i,new_j=i+dx,j+dy
                if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols or grid[new_i][new_j]==0 or visited[new_i][new_j]==1:
                    continue
                queue.append((new_i,new_j))
        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and visited[r][c]==0:
                    count+=1
        return count
        