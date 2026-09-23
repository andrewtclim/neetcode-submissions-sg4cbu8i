class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Uses a monotonically decreasing stack (lowest value on top of stack)
        By initializing the res array as 0's 
        """
        # init our result array 
        res = [0] * len(temperatures)
        # stack stores both [temp, index] 
        stack = []

        for i, t in enumerate(temperatures):
            # higher temperature case -> pop off stack then 
            # calculate and append the num of days it took to see this day
            while stack and t > stack[-1][0]:
                # isolate the days you want to update (last colder days)
                stackTemp, stackIndex = stack.pop()
                # append the calculated days in their respective days
                res[stackIndex] = i - stackIndex
            # lower or same temperatures get added on the top of stack 
            stack.append([t, i])
        
        return res


