# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.sameTree(root, root)
    def sameTree(self, leftT, rightT):
        if not leftT and not rightT:
            return True
        if leftT is None or rightT is None:
            return False
            
        return leftT.val == rightT.val and self.sameTree(leftT.left, rightT.right) and self.sameTree(leftT.right, rightT.left)
        