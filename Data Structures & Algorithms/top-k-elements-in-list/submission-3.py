from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for n in nums:
          d[n] += 1
        
        # after counting in dictionary d
        freq = [[] for _ in range(len(nums) + 1)]   # bucket indices = frequencies
        for num, count in d.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result