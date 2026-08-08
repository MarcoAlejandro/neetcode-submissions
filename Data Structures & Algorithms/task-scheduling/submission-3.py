from collections import Counter, defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        available = [ (t[1], t[0]) for t in Counter(tasks).items()]
        unavailable = []
        heapq.heapify_max(available)
        turn = 0
        while available or unavailable:

          if not available:
            turn = unavailable[0][0]

          while unavailable and unavailable[0][0] <= turn:
            c = heapq.heappop(unavailable)
            heapq.heappush_max( available, (c[1], c[2]) )
          
          if available:
            ex_left, T = heapq.heappop_max(available)
            if ex_left - 1 > 0:
              heapq.heappush(unavailable, (turn+n+1, ex_left-1, T))
            turn += 1

        return turn
        
        