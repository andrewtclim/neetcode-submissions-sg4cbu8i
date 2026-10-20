class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # init stack and res array 
        stack = [] # (temp, index)
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            # check when we found a warm day (process+update colder days)
            while stack and stack[-1][0] < t:
                waitTemp, waitIndex = stack.pop()
                res[waitIndex] = i - waitIndex
            # add the days to the top of stack 
            stack.append((t, i))
        
        return res