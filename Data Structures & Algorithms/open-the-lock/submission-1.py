class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        queue = deque(["0000"])
        visited = set(deadends)
        turns = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                lock = queue.popleft()
                if lock == target:
                    return turns
                for child in children(lock):
                    if child in visited:
                        continue
                    queue.append(child)
                    visited.add(child)
            turns += 1

        return -1

