# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Helper DFS function (Post-order traversal)
        def dfs(node):
            # Base case: reached end of branch
            if not node:
                return None
            # If current node is p or q, return it (found one target)
            if node == p or node == q:
                return node 
            # Search in left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            # Logic: If both sides returned a node, current is the split point (LCA)
            if left and right:
                return node
            # Otherwise, bubble up the non-null result (or None if neither found)
            return left if left else right
            
        return dfs(root)
