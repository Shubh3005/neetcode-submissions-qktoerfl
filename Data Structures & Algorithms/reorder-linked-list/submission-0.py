# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev= curr
            curr = nxt
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy= ListNode(-1)
        curr = head
        p1 = curr
        p2 = curr.next
        while p2 and p2.next:
            p1=p1.next
            p2 = p2.next.next
        p2 = self.reverse(p1.next)
        p1.next = None
        p1= curr
        cnt = 0
        node = dummy
        while p1 or p2:
            print(p1,p2)
            if cnt %2 == 0:
                node.next = p1
                p1 = p1.next
            elif cnt %2==1:
                node.next = p2
                p2 = p2.next
            cnt+=1
            node = node.next
        head = dummy.next