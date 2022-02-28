class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = Counter(nums)
        
        result = []
        for value, count in values.items():
            result.append((-1*count, value))
        heapify(result)
        
        return [heappop(result)[1] for i in range(k)]
        