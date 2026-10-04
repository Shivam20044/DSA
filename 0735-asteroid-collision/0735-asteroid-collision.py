class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        n=len(asteroids)
        result=[]
        for i in range(0,n):
            if asteroids[i]>0:
                result.append(asteroids[i])
            else:
                while result and result[-1]<abs(asteroids[i]) and result[-1]>0:
                    result.pop()
                
                if result and result[-1]==abs(asteroids[i]):
                    result.pop()
                
                elif len(result)==0 or result[-1]<0:
                    result.append(asteroids[i])
        return result
        