class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #total number of subset can be formed is 2^n subsets
        n=len(nums)
        total_subsets=1<<n
        result=[]
        for num in range(0,total_subsets): #tc=2^n
            list=[]
            for i in range(0,n): #tc=N
                if (num & (1<<i))!=0:
                    list.append(nums[i])
            result.append(list)
        return result
       #tc=O(N*2^n)
        