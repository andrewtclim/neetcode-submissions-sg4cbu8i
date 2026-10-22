# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # helper func
        def reverse(cur, prev):
            # base case
            if cur is None:
                return prev
            # recursive case
            else:
                # find temp next pointer 
                next = cur.next
                # reverse the order
                cur.next = prev
                return reverse(next, cur)
            
        # call helper func
        return reverse(head, None)