

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        
        # Initialize with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # We only need to go up to len(nums) - 2 because we need 3 items total
        for i in range(len(nums) - 2):
            
            # Skip duplicates for the fixed pointer 'i'
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                
                # Check if this sum is closer to the target than our previous best
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                    
                # Move pointers based on the sum
                if current_sum < target:
                    j += 1  # Sum is too small, need a larger number
                elif current_sum > target:
                    k -= 1  # Sum is too big, need a smaller number
                else:
                    # If the sum exactly equals the target, difference is 0. 
                    # You can't get closer than 0, so return immediately!
                    return current_sum
                    
        return closest_sum