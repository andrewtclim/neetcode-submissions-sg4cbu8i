# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case (empty list or last node)
        if not head or not head.next:
            return head
        
        # recursion case until last node
        newHead = self.reverseList(head.next)

        # reverse pointer
        head.next.next = head
        head.next = None

        return newHead