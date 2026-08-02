class Solution(object):
    def totalFruit(self, nums):
        """
        :type fruits: List[int]
        :rtype: int
        """
        dictt={}
        left=0
        right=0
        maxi=0
        while right<len(nums):
            dictt[nums[right]]=dictt.get(nums[right],0)+1
            if len(dictt)>2:
                dictt[nums[left]]-=1
                if dictt[nums[left]]==0:
                    del dictt[nums[left]]
                left+=1
            if len(dictt)<=2:
                maxi=max(maxi,right-left+1)
            right+=1
        return maxi

        