# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def reversePostOrder(root,level,ans):
            if root is None:
                return
            if len(ans)==level:
                ans.append(root.val)
            if root.right:
                reversePostOrder(root.right,level+1,ans)
            if root.left:
                reversePostOrder(root.left,level+1,ans)
        ans=[]
        reversePostOrder(root,0,ans)
        return ans

        