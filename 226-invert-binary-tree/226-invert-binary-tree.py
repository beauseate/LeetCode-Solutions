# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        
        left = root.right
        right = root.left
        
        root.left = self.invertTree(left)
        root.right = self.invertTree(right)
        
        
        return root
        
        
        