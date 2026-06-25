class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=0:
            return [-1,-1]
    
        def findFirst(nums,target):
            low=0
            high=len(nums)-1
            first=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    first=mid
                    high=mid-1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return first
        
        def findLast(nums,target):
            low=0
            high=len(nums)-1
            last=-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    last=mid
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            return last
        
        first=findFirst(nums,target)
        last=findLast(nums,target)
        return [first,last]
        