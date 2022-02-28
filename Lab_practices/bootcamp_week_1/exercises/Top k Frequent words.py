class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        values = Counter(words)
        result = []
        for value, count in values.items():
            result.append((-1*count, value))
        heapify(result)
        
        return [heappop(result)[1] for i in range(k)]