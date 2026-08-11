class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        L = 0
        ans = []
        while L < len(intervals):
            new_interval = intervals[L]
            while L + 1 < len(intervals) and new_interval[1] >= intervals[L+1][0]:
                new_interval[1] = max(new_interval[1], intervals[L+1][1])
                L += 1
            ans.append(new_interval)
            L += 1

        return ans