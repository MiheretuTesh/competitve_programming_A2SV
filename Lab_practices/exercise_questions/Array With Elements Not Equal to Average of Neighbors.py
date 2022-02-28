class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        s = len(nums)
        lst = []
        count = 1
        if(s<3):
            return nums
        else:    
            while(count < s-1):
                if((nums[count-1] + nums[count+1]) / 2 == nums[count]):
                    nums.append(nums.pop(count))
                    count = 1
                else:
                    count += 1
            return nums
            
soln = Solution()
print(soln.rearrangeArray([1, 2, 3, 4, 5]))
