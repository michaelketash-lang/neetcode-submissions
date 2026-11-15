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
        oldToNew = {None : None}
        cur = head
        while cur:
            val = cur.val
            nxt = cur.next
            rand = cur.random
            newNode = Node(val , nxt, rand)
            oldToNew[cur] = newNode
            cur = cur.next
        
        cur = head
        while cur:
            node = oldToNew[cur]
            node.next = oldToNew[cur.next]
            node.random = oldToNew[cur.random]
            cur = cur.next
        
        return oldToNew[head]




