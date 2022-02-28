class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lst = []
        for i in stones:
            lst.append(-1*i)
        heapify(lst)        
        while len(lst) >= 2:
            a = heappop(lst)
            b = heappop(lst)
            result = (-1*a) - (-1*b)
            print(result)
            lst.append(-1*result)
            heapify(lst)
        result = heappop(lst)
        return (-1*result)