# define a ListNode class
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

# define a LinkedList class
class LinkedList:
    
    def __init__(self):
        # maintain the head and tail pointers
        # Dummy Node (non empty ListNode)
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        # initalize current pointer (since we have dummy node -> starts at first head)
        curr = self.head.next
    
        # search through nodes (start at i=0 until i=index)
        i = 0 
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        # if our curr pointer reaches None -> index is out of bounds
        return -1

    def insertHead(self, val: int) -> None:
        # take val and convert it into a new node
        new_node = ListNode(val)
        # point this new node to the head 
        # remember self.head is currently the dummy node, so we need to get the next val 
        new_node.next = self.head.next
        # set new dummy to next node?
        self.head.next = new_node

        # edge case for an empty linked list (updates tail)
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        # Two cases both work 
        #1. empty list (tail points to dummy node) or 2. non-empty (point next tail to new val, update tail)
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0 
        # start at dummy node 
        curr = self.head
        # increments i until i=index and curr is not Null
        while i < index and curr:
            # moves curr to node before the target node
            i += 1
            curr = curr.next
        
        # check that target node and node before the target exists
        if curr and curr.next:
            # edge case -> target node = tail node, then set tail node as the node before target 
            if curr.next == self.tail:
                self.tail = curr

            # skips over the target node
            curr.next = curr.next.next
            return True
        
        # target index is out of bounds 
        return False


    def getValues(self) -> List[int]:
        # traverse through LinkedList and append values to an arr
        # initalize curr as the head pointer (start)
        curr = self.head.next
        res = []

        # until curr hits Null (end), append values to arr
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

