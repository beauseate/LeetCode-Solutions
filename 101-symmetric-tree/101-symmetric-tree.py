# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)
    def isMirror(self, leftRoot, rightRoot):
        if not leftRoot and not rightRoot: return True
        if not leftRoot or not rightRoot: return False
        return leftRoot.val == rightRoot.val and self.isMirror(leftRoot.left, rightRoot.right) and self.isMirror(leftRoot.right, rightRoot.left)
        