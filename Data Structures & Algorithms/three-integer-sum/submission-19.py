class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        First sort arr which takes O(n log n)
        Overall idea is that triplets a + b + c = 0 will be appended to our result
        Loop over and hold each a-value constant while scanning additional values b and c for valid triplets
        To find b and c values we apply two pointer method (twoSumII)
        After finding valid b, c pairs, we also slide and skip over any duplicate b values 
        This ensures skipping over any duplicate triplets (ie. a and b will be unique so will c)
        Time complexity is O(n^2) since there are two loops (outer loop for a and inner loop to scan for b, c)
        '''
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # skip over any duplicate a's (always process first a)
            if i > 0 and a == nums[i-1]:
                continue
            # init the l and r pointers (correspond with b and c)
            l = i + 1
            r = len(nums)-1
            # apply twoSum II scan 
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # ensure b is unique 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                # triplet too small -> increase
                elif threeSum < 0:
                    l += 1
                # triplet too large -> decrease
                else:
                    r -= 1
        
        return res
                
