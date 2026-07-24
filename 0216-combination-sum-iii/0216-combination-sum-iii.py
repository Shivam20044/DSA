class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums=[1,2,3,4,5,6,7,8,9]
        result=[]
        def fun(index,total,count,subset):
            if count==k:
                if total==n:
                    result.append(subset[:])
                return
            elif index>=len(nums) or total>n or count>k:
                return
            total=total+nums[index]
            subset.append(nums[index])
            fun(index+1,total,count+1,subset)
            total=total-nums[index]
            subset.pop()
            fun(index+1,total,count,subset)
        
        fun(0,0,0,[])
        return result
        