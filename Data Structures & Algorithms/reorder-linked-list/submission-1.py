# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # 1. Find the middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            front = second.next
            second.next = prev
            prev = second
            second = front

        second = prev

        # 3. Merge the two halves
        first = head

        while second:
            temp1 , temp2 = first.next , second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
