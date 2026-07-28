import heapq

class MedianFinder:
    def __init__(self):
        self._left_heap = []   # max-heap (store negatives)
        self._right_heap = []  # min-heap

    def addNum(self, num: int) -> None:
        # Step 1: push to left heap (max-heap via negation)
        heapq.heappush(self._left_heap, -num)

        # Step 2: ensure left's max <= right's min
        if self._left_heap and self._right_heap:
            if -self._left_heap[0] > self._right_heap[0]:
                val = -heapq.heappop(self._left_heap)
                heapq.heappush(self._right_heap, val)

        # Step 3: rebalance sizes – left can be at most 1 larger
        if len(self._left_heap) > len(self._right_heap) + 1:
            val = -heapq.heappop(self._left_heap)
            heapq.heappush(self._right_heap, val)
        elif len(self._right_heap) > len(self._left_heap):
            val = heapq.heappop(self._right_heap)
            heapq.heappush(self._left_heap, -val)

    def findMedian(self) -> float:
        if len(self._left_heap) > len(self._right_heap):
            return float(-self._left_heap[0])
        else:
            return (-self._left_heap[0] + self._right_heap[0]) / 2.0