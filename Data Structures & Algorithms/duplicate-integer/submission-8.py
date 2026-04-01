class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize hashset
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        # no duplicate found
        return False
        