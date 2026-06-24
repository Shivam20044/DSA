class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()

        result=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                k=j+1
                l=len(nums)-1
                while k<l:
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if target>sum:
                        k+=1
                    elif target<sum:
                        l-=1
                    else:
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        result.append(temp)
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while l>k and nums[l]==nums[l+1]:
                            l-=1
                    
                
        return result
         

        