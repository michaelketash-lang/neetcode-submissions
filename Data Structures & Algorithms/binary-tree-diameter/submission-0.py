# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diamater = [0]
        def dfs(root):
            if not root:
                return 0
            
            left_child = dfs(root.left)
            right_child = dfs(root.right)
            diameter = left_child + right_child

            largest_diamater[0] = max(largest_diamater[0],diameter)
            return 1 + max(left_child,right_child)
        dfs(root)
        return largest_diamater[0]