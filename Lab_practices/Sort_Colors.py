class Solution(object):
    def sortColors(self, nums):
        
        for i in range(0, len(nums)):
            min = i
            for j in range(i+1, len(nums)):
                if(nums[j]<nums[min]):
                    min = j
            nums[i], nums[min] = nums[min], nums[i]
        return nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        