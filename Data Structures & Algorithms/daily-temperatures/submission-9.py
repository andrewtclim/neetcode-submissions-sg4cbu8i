class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # utilize a montonically decreasing stack 
        # top of stack is always the coldest day(warmest day stays at bottom)

        stack = [] # (temp, index)
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            # warm day case -> process colder days 
            while stack and t > stack[-1][0]:
                # extract values from colder day 
                waitTemp, waitIndex = stack.pop()
                res[waitIndex] = i - waitIndex
            
            # add the new temp to stack 
            stack.append((t, i))
        
        return res
