# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # RECURSIVE SOLUTION 
        def reverse(curr, prev):
            # base case - stop when reaches the end of the LL
            if curr is None:
                return prev
            else:
                # track forward direction's next node
                nxt = curr.next 
                # reverse the order 
                curr.next = prev 
                # apply function to next pair of nodes
                return reverse(nxt, curr)
        
        return reverse(head, None)

