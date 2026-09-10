# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #dummy node to handle edge cases
        dummy = ListNode(0)
        cur = dummy
        carrier = 0 #reminder
        while l1 or l2 or carrier: #if one of this alive need to keep calculate
            v1 = l1.val if l1 else 0 #if dont have val compute with 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carrier #calculate total
            new_val = total % 10 #calculate new_val
            carrier = total // 10
            new_node = ListNode(new_val)
            cur.next = new_node
            cur = cur.next
            #keep moving if still have nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
        