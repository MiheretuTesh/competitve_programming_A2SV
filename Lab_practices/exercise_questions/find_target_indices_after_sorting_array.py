class Solution(object):
    def targetIndices(self, nums, target):

        indice = []
        for i in range(0, len(nums)):
            min = i
            for j in range(i+1, len(nums)):
                if(nums[min] > nums[j]):
                    min = j
            nums[i], nums[min] = nums[min], nums[i]
        print(nums)
        
        for i in range(0, len(nums)):
            if target==nums[i]:
                indice.append(i)

        return indice


soln = Solution()
print(soln.targetIndices([2, 4, 6, 6, 1, 5], 6))
