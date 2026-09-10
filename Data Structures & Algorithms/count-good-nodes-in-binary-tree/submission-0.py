# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #Another function inorder to pass maxval so far
        def dfs(curr,max_val):
            # no good nodes if empty.
            if not curr:
                return 0
            #add 1 cuase cur value greater than max
            res = 1 if curr.val >= max_val else 0
            #take max between cur and max
            max_val = max(max_val,curr.val)
            # Preorder traversal
            res += dfs(curr.left,max_val)
            res += dfs(curr.right,max_val)
            return res

        return dfs(root,root.val)

        