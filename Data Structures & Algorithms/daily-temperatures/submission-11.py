class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # monotonically decreasing stack 
        # aka stack always keeps coldest days at top and warmest at bottom 

        stack = [] # (temp, index)
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            # found warm day case (process)
            while stack and t > stack[-1][0]:
                # isolate the processed days temp and index
                waitTemp, waitIndex = stack.pop()
                # calc and append the waited days 
                res[waitIndex] = i - waitIndex
            # otherwise keep adding colder days to top of stack 
            stack.append((t, i))

        return res