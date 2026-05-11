class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-val for val in stones]
        heapq.heapify(stones)
        print(stones)

        diff = 0
        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if y > x:
                heapq.heappush(stones, x - y)

        stones.append(0)
        return abs(stones[0])
