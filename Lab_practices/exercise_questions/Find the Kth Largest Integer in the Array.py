class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        lst =nums
        lst.sort(key = lambda x: int(x), reverse=True)
        
        return lst[k-1]
            
soln  = Solution()
print(soln.kthLargestNumber(["3","6","7","10"], 4))