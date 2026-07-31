class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        right=0
        left=0
        n=len(nums)
        maxi=0
        count=0
        while right<n:
            if nums[right]==0:
                count+=1
            if count>k:
                if nums[left]==0:
                    count-=1
                left+=1
            if count<=k:
                maxi=max(maxi,right-left+1)
            right+=1
        
        return maxi

        