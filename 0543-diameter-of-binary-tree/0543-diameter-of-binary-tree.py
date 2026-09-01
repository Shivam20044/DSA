class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0  # Reset to 0 for every new test case
        
        # Helper function dedicated strictly to calculating height
        def calculate_height(node):
            if node is None:
                return 0
            
            leftHeight = calculate_height(node.left)
            rightHeight = calculate_height(node.right)
            
            # Update the global max diameter using the heights
            self.diameter = max(self.diameter, leftHeight + rightHeight)
            
            # Return height up to the parent
            return 1 + max(leftHeight, rightHeight)
            
        # 1. Kick off the recursion
        calculate_height(root)
        
        # 2. Return the actual requested answer
        return self.diameter