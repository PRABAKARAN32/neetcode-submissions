# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return
        
        # Find the mid

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # the slow in the end of the first linked list
        second = slow.next
        # Disconnect the first-half of the linked list
        slow.next = None


        # Revers the second half
        prev = None

        while second:
            nxet = second.next
            second.next = prev
            prev = second
            second = nxet
        
        # Merge the linked list
        left = head
        right = prev

        while right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next