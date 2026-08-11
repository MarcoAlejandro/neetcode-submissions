from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [ (count, number) for number, count in Counter(nums).items()]
        heapq.heapify_max(counts)
        output = []
        while k > 0:
            output.append(heapq.heappop_max(counts)[1])
            k -= 1

        return output
        