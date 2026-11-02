# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init pointers 
        prev, curr = None, head

        while curr:
            nxt = curr.next 

            # reverse pointer
            curr.next = prev 

            # update pointers
            prev = curr 
            curr = nxt 

        # new head is at prev 
        return prev