"""

Approach number 1
1. Sort the array, using the distance as sort criteria -> O(log n)
2. Retrieve K elems. -> O(k)
total runtime = O(log n) + O(k)


Approach number 2
1. Heap, Heapify -> O(n)
2. retrieve k elem -> K O(Log n)
T(n) = O(n) + KO(log n)

"""
import heapq
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, point):
        self_d = math.sqrt( 
            ((self.x - 0) * (self.x - 0)) +  ((self.y - 0) * (self.y - 0))
        )
        other_d = math.sqrt( 
            ((point.x - 0) * (point.x - 0)) +  ((point.y - 0) * (point.y - 0))
        )
        return self_d < other_d
        

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [Point(p[0], p[1]) for p in points]
        heapq.heapify(points)
        ans = []
        for _ in range(k):
            elem = heapq.heappop(points)
            ans.append((elem.x, elem.y))
        return ans


