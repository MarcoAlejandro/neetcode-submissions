from collections import Counter
from collections import deque


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [deque() for _ in range(len(nums) + 1)]
        ans = []
        for N, count in counts.items():
            buckets[count].append(N)
        
        index = len(nums)
        while k > 0:
            if buckets[index]:
                ans.append(buckets[index].popleft())
                k -= 1
            else:
                index -= 1

    
        return ans
