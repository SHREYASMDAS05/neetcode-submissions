# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head

        # Find node before left
        before = dummy
        for _ in range(left - 1):
            before = before.next

        # Start of section
        start = before.next

        # Find node after right
        end = start
        for _ in range(right - left):
            end = end.next

        after = end.next

        prev = after
        curr = start

        for _ in range(right - left + 1):
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        before.next = prev

        return dummy.next