# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init pointers
        prev, curr = None, head

        # run algo until curr hits None
        while curr:
            # track a nxt pointer (to keep forward direction)
            nxt = curr.next

            # reverse pointer
            curr.next = prev 

            # update pointers
            prev = curr # move prev to the next spot
            curr = nxt  # move curr to next spot 
        
        return prev # prev becomes the new head
