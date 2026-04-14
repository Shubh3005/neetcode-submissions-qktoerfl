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
        # The new list initialized
        dummy= ListNode(-1)
        # Keep head the same create new variable to traverse throught LL
        curr = head
        # Create two pointers (Tortise and Hare) for finding middle of the Linked List
        p1 = curr
        p2 = curr.next
        while p2 and p2.next:
            p1=p1.next
            p2 = p2.next.next
        # Flip second half of array 
        p2 = self.reverse(p1.next)
        # Break off array so we have two linked lists
        p1.next = None
        # Reset start of p1
        p1= curr
        # Now we have the main algo where we are alternating between p1 and p2
        # we are adding to our dummy list so we can have our result
        # cnt = 0
        node = dummy
        p1 = head
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next

            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2

            # if cnt %2 == 0:
            #     node.next = p1
            #     p1 = p1.next
            # elif cnt %2==1:
            #     node.next = p2
            #     p2 = p2.next
            # cnt+=1
            # node = node.next
        # head = dummy.next