from typing import List, Tuple
from bisect import bisect_left

class MyCalendar:
    
    def __init__(self):
        self._events: List[Tuple[int, int]] = []

    def book(self, startTime: int, endTime: int) -> bool:
        idx = bisect_left(self._events, (startTime, endTime))

        if idx > 0 and self._events[idx - 1][1] > startTime:
            return False
        
        if idx < len(self._events) and self._events[idx][0] < endTime:
            return False
        
        self._events.insert(idx, (startTime, endTime))
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)