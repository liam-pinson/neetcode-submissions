class Solution:

    def distance(self, point: List) -> float:
        return (point[0] ** 2) + (point[1] ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_arr = []
        for point in points:
            d = self.distance(point)
            dist_arr.append([d, point[0], point[1]])

        heapq.heapify(dist_arr)
        print(dist_arr)

        sol = []
        for _ in range(k):
            dist, x, y = heapq.heappop(dist_arr)
            sol.append([x, y])

        return sol