class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        n = len(startTime)
        max_profit = [0]*n
        prev_best = 0
        events = list()
        START, END = 1, 0
        # do using line sweep
        # sort the events like start and end
        for idx, (start, end) in enumerate(zip(startTime, endTime)):
            events.append((start, START, idx))
            events.append((end, END, idx))
        events.sort()
        # if it is start event take the sum of profit and prev_best else just update the prev_best
        for x, e, idx in events:
            if e == START:
                max_profit[idx] = max(max_profit[idx], profit[idx]+prev_best)
            else:
                prev_best = max(prev_best, max_profit[idx])

        return max(max_profit)
