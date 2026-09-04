from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(mat)
        c = len(mat[0])
        visited = [[0 for _ in range(c)] for _ in range(r)]
        distance = [[0 for _ in range(c)] for _ in range(r)]
        queue = deque()
        
        # Multi-source BFS: Add all 0s to the queue first
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    queue.append([i, j, 0])
                    visited[i][j] = 1
                    
        while queue:
            i, j, dis = queue.popleft()
            distance[i][j] = dis
            
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_i, new_j = i + x, j + y
                
                # FIX 1: The 'continue' must happen if it IS out of bounds
                if new_i < 0 or new_i >= r or new_j < 0 or new_j >= c:
                    continue
                    
                # FIX 2: This block must be OUTSIDE the boundary check
                if visited[new_i][new_j] == 1:
                    continue
                    
                queue.append([new_i, new_j, dis + 1])
                
                # FIX 3: Use assignment (=), not equality (==)
                visited[new_i][new_j] = 1 
                
        return distance