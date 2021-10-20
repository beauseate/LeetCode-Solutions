# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.sym(root, root)
    def sym(self, leftRoot, rightRoot):
        if not leftRoot and not rightRoot:
            return True
        if not leftRoot or not rightRoot:
            return False
        
        return leftRoot.val == rightRoot.val and self.sym(leftRoot.left, rightRoot.right) and self.sym(leftRoot.right, rightRoot.left)
        