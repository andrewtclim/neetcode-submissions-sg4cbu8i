class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # init result array and monotonically decreasing stack
        res = [0] * len(temps)
        stack = [] # tuples of (temp, index)

        for i, t in enumerate(temps):
            # if we've found a new warm day, process all the old cold days 
            while stack and stack[-1][0] < t:
                # calc the number of days that day has been waiting 
                waitTemp, waitIndex = stack.pop()
                res[waitIndex] = (i - waitIndex)
            # when we find new days append them to stack to be processed
            stack.append((t, i))
        
        return res
