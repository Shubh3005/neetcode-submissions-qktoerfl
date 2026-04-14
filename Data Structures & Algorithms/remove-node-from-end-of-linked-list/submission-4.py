# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        p1= dummy
        p2 = dummy
        while n>0:
            p2 = p2.next
            n-=1
        while p2 and p2.next:
            p1= p1.next
            p2=p2.next
        p1.next = p1.next.next
        print(p2.val)
       
        return dummy.next