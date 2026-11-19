# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init the curr and prev of the LL
        curr, prev = head, None

        # apply algo until we hit the end of the LL
        while curr:
            # track forward direction next node
            nxt = curr.next 

            # reverse the curr's pointer
            curr.next = prev

            # update pointers
            prev = curr
            curr = nxt

        return prev
