# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2 or carry: #crry is to deal with 8 + 7 = 15 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            new_val = v1 + v2 + carry
            carry = new_val // 10
            new_val %= 10 
            curr.next = ListNode(new_val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
            

