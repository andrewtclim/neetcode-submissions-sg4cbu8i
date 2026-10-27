# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init prev and curr pointers
        prev, curr = None, head

        while curr:
            # from original order (track nxt)
            nxt = curr.next 

            # reverse pointer 
            curr.next = prev 

            # update pointers
            prev = curr
            curr = nxt

        return prev
