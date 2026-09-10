# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0 :
            return
        # run in while loop on length of lists
        while len(lists) > 1 :
            merged = []
            #run in inner loop on two sublists and merge them
            for i in range(0,len(lists),2):
                lst1 = lists[i]
                lst2 = lists[i + 1] if (i+1) < len(lists) else None
                merged.append(self.merge2lsts(lst1,lst2))
            lists = merged # update lists to be the merged array
        return lists[0]
    #merge two lists
    def merge2lsts(self,lst1,lst2):
        dummy = ListNode()
        cur = dummy
        while lst1 and lst2:
            if lst1.val < lst2.val:
                cur.next = lst1
                lst1 = lst1.next
            else:
                cur.next = lst2
                lst2 = lst2.next
            cur = cur.next
        if lst1:
            cur.next = lst1
        if lst2:
            cur.next = lst2
        return dummy.next

