import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = [-1*i for i in stones]
        heapq.heapify(res)
        while len(res)>1:
            a = heapq.heappop(res)
            b = heapq.heappop(res)
            heapq.heappush(res,-1*abs(a-b))
        return -1*res[0]
