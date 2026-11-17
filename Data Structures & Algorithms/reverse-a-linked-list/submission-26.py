# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr, prev):
            # base case 
            if not curr:
                return prev
            # recursive case
            else:
                nxt = curr.next  # identify next value
                curr.next = prev # swap order

                return reverse(nxt, curr) # apply next recursive call
        
        return reverse(head, None)