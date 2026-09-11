class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    island.append((i,j))
        count=0
        visited=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue=deque()
        for i,j in island:
            if visited[i][j]==1:
                continue
            visited[i][j]=1
            count+=1
            queue.append((i,j))
            while queue:
                a,b=queue.popleft()
                
                for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    new_a,new_b=a+dx,b+dy
                    if new_a<0 or new_a>=len(grid) or new_b<0 or new_b>=len(grid[0]):
                        continue
                    if visited[new_a][new_b]==1 or grid[new_a][new_b]=="0":
                        continue
                    queue.append((new_a,new_b))
                    visited[new_a][new_b]=1
        return count



        