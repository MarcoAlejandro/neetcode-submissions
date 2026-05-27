
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        answer = 1000000000
        l = 1
        r = max(piles)

        while l <= r:
          k = l + (r-l) // 2
          sum_ = sum( map( lambda p: (p+k-1) // k, piles  ) )
          if sum_ > h:
            l = k + 1
          else:
            answer = min(answer, k)
            r = k - 1
        
        return answer
