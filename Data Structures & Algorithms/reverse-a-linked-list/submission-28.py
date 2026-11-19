# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr, prev):
            # base case (stop when curr hits None)
            if not curr:
                return prev
            # recursive case
            else:
                # find the nxt pointer
                nxt = curr.next
                # reverse pointer 
                curr.next = prev 
                # next call 
                return reverse(nxt, curr)
        
        return reverse(head, None)
