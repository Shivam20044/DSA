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
        val=image[sr][sc]
        vis=deepcopy(image)
        r,c=len(vis),len(vis[0])
        intial_color=vis[sr][sc]
        def dfs(i,j,new_color,initial_color,vis,r,c):
            if i<0 or i>=r or j<0 or j>=c:
                return
            if vis[i][j]!=intial_color:
                return
            if vis[i][j]==new_color:
                return
            vis[i][j]=new_color
            dfs(i+1,j,new_color,initial_color,vis,r,c)
            dfs(i,j-1,new_color,initial_color,vis,r,c)
            dfs(i-1,j,new_color,initial_color,vis,r,c)
            dfs(i,j+1,new_color,initial_color,vis,r,c)
        dfs(sr,sc,color,intial_color,vis,r,c)
        return vis
     
                

            
            

        