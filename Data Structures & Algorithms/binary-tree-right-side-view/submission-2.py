from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])

        while queue:
            right_view = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    right_view = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if right_view:
                res.append(right_view.val)
        return res


        