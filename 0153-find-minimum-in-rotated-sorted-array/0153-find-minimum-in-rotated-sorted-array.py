class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high=0,len(nums)-1
        minimum=float("inf")
        if(nums[low]<nums[high]):
            return nums[low]
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                minimum=min(minimum,nums[mid])
                high=mid-1
            else:
                minimum=min(minimum,nums[mid])
                low=mid+1
        return minimum


        