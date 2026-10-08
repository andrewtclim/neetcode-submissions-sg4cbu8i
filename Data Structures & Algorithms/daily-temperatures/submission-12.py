class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # monotonically decreasing stack 
        stack = [] # (temp, index)
        res = [0]*len(temps)

        for i, t in enumerate(temps):
            # when we find hot days (process all the colder days)
            while stack and stack[-1][0] < t:
                waitTemp, waitIndex = stack.pop()
                res[waitIndex] = i - waitIndex
            # colder days than the last cold day -> apend to top 
            stack.append((t, i))
        
        return res
