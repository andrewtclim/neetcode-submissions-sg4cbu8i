# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init the prev and curr pointers in our LL
        prev, curr = None, head

        # run until we hit the end of our LL
        while curr:
            # keep track of the next pointer (apply algo in og forward direction)
            nxt = curr.next 

            # reverse the link
            curr.next = prev

            # update pointers 
            prev = curr
            curr = nxt
        
        # prev ends up as the new head 
        return prev