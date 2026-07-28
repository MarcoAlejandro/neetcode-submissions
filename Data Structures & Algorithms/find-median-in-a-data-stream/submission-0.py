"""[1, 2, 3, 4]

4 // 2 = 2
(4 // 2) - 1  = 1

[1, 2]
2 // 2 = 1
2 // 2 - 1 = 0
"""

import bisect

class MedianFinder:

    def __init__(self):
        self._nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self._nums, num)  # -> Cost: search O(logn) + insert O(n) 

    def findMedian(self) -> float:
        if len(self._nums) % 2 == 0:
            return (
                (self._nums[len(self._nums)//2] + self._nums[len(self._nums)//2-1]) / 2 
            )
        else:
            return self._nums[len(self._nums)//2]

        