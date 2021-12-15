class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """

        nums = nums.sort(key = lambda x: x)
        return nums
        # return nums.index()
            
soln  = Solution()
print(soln.kthLargestNumber(["3","6","7","10"], 4))