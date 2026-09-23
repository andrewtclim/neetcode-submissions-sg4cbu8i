class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Monotonic decreasing stack (stack[-1] is the most recent cold day) 
        The stack holds indices of days still "waiting" for a warmer day. 
        When today's temp beats a waiting day,
        we know how long that day waited (i - waitingIdx).

        - Stack stores (temp, index) tuples, decreasing temp from bottom to top.
        - res defaults to 0, so any index left on the stack at the end (no
          warmer day ever came) correctly stays at 0.
        - O(n) time: each index is pushed and popped at most once.
        """
        res = [0] * len(temperatures)
        stack = []  # list of (temp, index)

        for i, t in enumerate(temperatures):
            # found a new warmer day than the stack's top -> resolve waits
            while stack and t > stack[-1][0]:
                # last waiting temp and index
                waitingTemp, waitingIdx = stack.pop()
                # calc the wait time for this day
                res[waitingIdx] = i - waitingIdx
            stack.append((t, i))

        return res
