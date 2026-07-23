class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def fun(index,total,subset):
            if total==target:
                result.append(subset[:])
                return
            if total>target:
                return
            elif index>=len(candidates):
                return
            summ=total+candidates[index]
            subset.append(candidates[index])
            fun(index,summ,subset)
            subset.pop()
            summ=total
            fun(index+1,summ,subset)
        
        result=[]
        fun(0,0,[])
        return result