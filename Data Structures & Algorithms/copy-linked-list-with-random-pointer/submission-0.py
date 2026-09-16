"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # approach: Hash map
        # key : old node val: new node
        mapi = {None : None} #to handle edge cases
        cur = head
        while cur:
            copy = Node(cur.val)
            mapi[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = mapi[cur]
            copy.next = mapi[cur.next]
            copy.random = mapi[cur.random]
            cur = cur.next
        return mapi[head]
            
