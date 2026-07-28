import heapq


class MedianFinder:
    def __init__(self):
        self._left_heap = []   # Max-heap
        self._right_heap = []  # Min-heap

    def addNum(self, num: int) -> None:
        # Step 1: push directly into the max-heap
        heapq.heappush_max(self._left_heap, num)

        # Step 2: ensure every left value <= every right value
        if (
            self._right_heap
            and self._left_heap[0] > self._right_heap[0]
        ):
            val = heapq.heappop_max(self._left_heap)
            heapq.heappush(self._right_heap, val)

        # Step 3: rebalance sizes
        # Left may contain at most one extra element
        if len(self._left_heap) > len(self._right_heap) + 1:
            val = heapq.heappop_max(self._left_heap)
            heapq.heappush(self._right_heap, val)

        elif len(self._right_heap) > len(self._left_heap):
            val = heapq.heappop(self._right_heap)
            heapq.heappush_max(self._left_heap, val)

    def findMedian(self) -> float:
        if len(self._left_heap) > len(self._right_heap):
            return float(self._left_heap[0])

        return (self._left_heap[0] + self._right_heap[0]) / 2.0