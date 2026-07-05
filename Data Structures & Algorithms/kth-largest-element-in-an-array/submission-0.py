import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)

        popd = -1
        for i in range(k):
            popd = heapq.heappop(heap)
        
        return -popd