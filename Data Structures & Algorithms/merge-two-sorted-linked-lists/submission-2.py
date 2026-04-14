# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        p1= list1
        p2 = list2
        while p1 or p2:
            if not p2 or (p1 and p1.val<p2.val):
                curr.next = p1
                p1=p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        return dummy.next