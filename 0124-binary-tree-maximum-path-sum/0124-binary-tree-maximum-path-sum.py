class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 1. Handle trees where ALL nodes are negative
        self.maxsum = -float('inf')
        
        # 2. Dedicated helper function for the recursive math
        def get_max_branch(node):
            if node is None:
                return 0
            
            # Get max branch sums, defaulting to 0 if they are negative
            # (This is a cleaner way to write your if lSum < 0 logic!)
            lSum = max(get_max_branch(node.left), 0)
            rSum = max(get_max_branch(node.right), 0)
            
            # Update the global max path found so far (the "V" path)
            self.maxsum = max(self.maxsum, lSum + node.val + rSum)
            
            # Return the max single branch that the parent can use
            return node.val + max(lSum, rSum)
            
        get_max_branch(root)
        return self.maxsum