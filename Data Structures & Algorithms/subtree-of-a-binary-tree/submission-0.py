# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.same(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

    

    def same(self,first,sec):
        if not first and not sec:
            return True
        if not first or not sec:
            return False
        return ((first.val == sec.val) and self.same(first.left,sec.left) and self.same(first.right,sec.right))

        