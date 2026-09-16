# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseLst(self , head:Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        # Lets break it into steps:
        if not head or not head.next:
            return

        # first - we want to find node before the middle
        cur = self.findMid(head)
        sec_half = cur.next
        # second - we want to break the link between mid
        cur.next = None
        # reverse the seconde half of linked list
        sec_half = self.reverseLst(sec_half) #sec_half is the new head of the reversed linked list
        # scan together and add it to new list
        cur = head
        while cur and sec_half:
            temp1 = cur.next
            temp2 = sec_half.next
            cur.next = sec_half
            sec_half.next = temp1
            sec_half = temp2
            cur = temp1











