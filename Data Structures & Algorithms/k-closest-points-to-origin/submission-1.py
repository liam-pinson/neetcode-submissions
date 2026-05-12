class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(point):
            return point[0]**2 + point[1]**2
        
        point_dist = []
        for point in points:
            point_dist.append([distance(point), point[0], point[1]])

        heapq.heapify(point_dist)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(point_dist)
            res.append([x, y])
            k -= 1

        return res