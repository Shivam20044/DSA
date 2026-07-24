class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        result=[]
        def fun(last,total,count,subset):
            if count==k and total==n:
                result.append(subset[:])
                return
            elif last>=10 or count>k or total>n:
                return
            for i in range(last,10):
                total=total+i
                subset.append(i)
                fun(i+1,total,count+1,subset)
                total=total-i
                subset.pop()
    
        fun(1,0,0,[])
        return result



        