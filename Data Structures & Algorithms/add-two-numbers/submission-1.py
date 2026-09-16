# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # notice: 
        # 1. need to handle carry for example : 9 + 5 = 4 , carry = 1
        # 2. problem : diffrent length solution: padding with 0
        dummy = ListNode()
        res = dummy
        cur1 = l1
        cur2 = l2
        carry = 0
        while cur1 or cur2 or carry:
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0
            new_val = val1 + val2 + carry
            carry = new_val // 10
            new_val = new_val % 10
            res.next = ListNode(new_val)
            res = res.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
        

        return dummy.next
        