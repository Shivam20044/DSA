class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 1. CRUCIAL: Sort the candidates first so duplicates line up
        candidates.sort()
        result = []
        
        # 2. Define the helper function INSIDE so it can access 'result'
        def backtrack(index, total, subset):
            if total == 0:
                result.append(subset[:])
                return
            if total < 0 or index >= len(candidates):
                return

            for i in range(index, len(candidates)):  # Fixed: changed 'nums' to 'candidates'
                # Skip duplicate elements at the same decision depth
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                    
                subset.append(candidates[i])
                # Recurse: reduce target by the chosen number, move to index i + 1
                backtrack(i + 1, total - candidates[i], subset)
                subset.pop()  # Undo choice (backtrack)

        # 3. Kick off the recursion
        backtrack(0, target, [])
        return result