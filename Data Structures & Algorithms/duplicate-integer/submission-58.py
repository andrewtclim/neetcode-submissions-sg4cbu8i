class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # init a hashset 
        hashset = set()

        # iter over nums 
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        
        return False