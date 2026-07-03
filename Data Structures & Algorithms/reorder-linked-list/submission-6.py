# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        def reverse(head):
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        # Find middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = reverse(slow.next)
        slow.next = None

        first = head

        # Merge
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2