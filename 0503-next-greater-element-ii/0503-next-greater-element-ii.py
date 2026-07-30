class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[-1 for _ in range(n)]
        stack=[]
        for i in range(2*n-1,-1,-1):
            current_num=nums[i%n]

            while len(stack) != 0 and stack[-1] <= current_num:
                stack.pop()

            if i < n:
              if len(stack) != 0:
                ans[i] = stack[-1]

            stack.append(current_num)
        
        return ans

            
        