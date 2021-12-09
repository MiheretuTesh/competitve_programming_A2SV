class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        compare = []
        for i in range(0, len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if j != i:
                    if(nums[i]>nums[j]):
                        count += 1
            compare.append(count)
            count = 0
        return compare
    
soln =Solution()
print(soln.smallerNumbersThanCurrent([7,7,7,7]))