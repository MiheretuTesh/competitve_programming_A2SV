class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []
        for i in nums:
            result.append(-1*i)
        heapify(result)
        for i in range(k):
            a = heappop(result)
        return (-1*a)