from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        dict1 = Counter(nums)
        a = max(dict1)
        print(dict1)
        b = list(dict1)
        lst = []
        for i in range(k):
            print(b[i])
           
        return b

soln = Solution()
print(soln.topKFrequent([1,2,2,2,3,4,5,5,5,5], 2))
