import heapq


class KthLargest:
    def __init__(self, k: int, nums):
        self.pool = heapq.nlargest(k, nums)[::-1]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


class KthLargest:
    def __init__(self, k: int, nums):
        self.pool = sorted(nums)[-k:]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            self.pool.append(val)
            self.pool = sorted(self.pool)
        elif val > self.pool[0]:
            self.pool.pop(0)
            self.pool.append(val)
            self.pool = sorted(self.pool)
        return self.pool[0]


k = KthLargest(2, [0])
print(k.add(-1))
# k=heapq.nlargest(3,[3,4,5,7,9])
# print(k)
# heapq.heappushpop(k,8)
# print(k)
["KthLargest", "add", "add", "add", "add", "add"]
[[2, [0]], [-1], [1], [-2], [-4], [3]]

# print([1, 3, 5, 7, 9][-13:])
