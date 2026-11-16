class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # init stack and res
        stack = [] # (day_index, day_temp)
        res = [0]*len(temps)

        for i, t in enumerate(temps):
            # process all colder days than the current day 
            while stack and stack[-1][1] < t:
                waitI, waitT = stack.pop()
                # update the day on the res
                res[waitI] = i - waitI
            # update the top of the stack 
            stack.append((i, t))
        
        return res