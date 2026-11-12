# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr, prev):
            # base case
            if curr is None:
                return prev
            
            # recursive case 
            else:
                # flip pointers for curr
                nxt = curr.next 
                curr.next = prev 
                # move on to next pair of nodes
                return reverse(nxt, curr)
        
        # start recursive func with head as curr and None as prev
        return reverse(head, None)