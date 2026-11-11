# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init prev and curr
        prev, curr = None, head

        # iter until end of list
        while curr:
            # track forward direction
            nxt = curr.next

            # reverse pointer
            curr.next = prev

            # update positions
            prev = curr
            curr = nxt
        
        # prev ends as the new head of the LL
        return prev 
