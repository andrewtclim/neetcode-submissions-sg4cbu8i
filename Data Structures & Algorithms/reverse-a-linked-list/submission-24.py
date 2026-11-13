# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, curr):
            # base case 
            if curr == None:
                return prev 
            # recursive case 
            else:
                nxt = curr.next 
                curr.next = prev 
                return reverse(curr, nxt)
        
        return reverse(None, head)