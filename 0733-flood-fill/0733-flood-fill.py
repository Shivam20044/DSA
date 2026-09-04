from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if color==image[sr][sc]:
            return image
        
        vis=deepcopy(image)
        val=vis[sr][sc]
        r,c=len(vis),len(vis[0])
        queue=deque()
        queue.append((sr,sc))
        while queue:
            i,j=queue.popleft()
            vis[i][j]=color
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                new_i,new_j=i+dx,j+dy
                if new_i<0 or new_i>=r or new_j<0 or new_j>=c or vis[new_i][new_j]==color or vis[new_i][new_j]!=val:
                    continue
                queue.append((new_i,new_j))
        return vis



            
            

        