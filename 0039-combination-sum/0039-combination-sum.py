class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 1. Sort candidates so we can prune early
        candidates.sort()
        result = []
        
        def backtrack(start_index, current_target, subset):
            # Base Case: We hit the exact target
            if current_target == 0:
                result.append(subset[:])
                return
            
            for i in range(start_index, len(candidates)):
                # 2. PRUNING: If the current number is bigger than what we need,
                # because the list is sorted, every number after it will also be too big!
                if candidates[i] > current_target:
                    break
                
                subset.append(candidates[i])
                # 3. REUSE ELEMENT: Pass 'i' instead of 'i + 1' so the same number can be picked again
                backtrack(i, current_target - candidates[i], subset)
                subset.pop() # Backtrack

        backtrack(0, target, [])
        return result