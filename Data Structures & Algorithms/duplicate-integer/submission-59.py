class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # init hashset 
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        
        return False