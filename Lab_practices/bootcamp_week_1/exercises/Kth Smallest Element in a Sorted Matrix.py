class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result = []
        for i in matrix:
            for j in i:
                result.append(j)
        heapify(result)
        for i in range(k-1):
            heappop(result)
        return heappop(result)